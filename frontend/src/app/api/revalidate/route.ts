import { revalidatePath, revalidateTag } from "next/cache";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const auth = request.headers.get("Authorization");
  const secret = process.env.REVALIDATE_SECRET;

  if (!secret || auth !== `Bearer ${secret}`) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const body = await request.json().catch(() => ({}));
  const paths: string[] = body.paths ?? [];
  const tags: string[] = body.tags ?? [];

  if (paths.length === 0 && tags.length === 0) {
    return NextResponse.json({ error: "paths or tags required" }, { status: 400 });
  }

  for (const tag of tags) {
    revalidateTag(tag);
  }
  for (const path of paths) {
    revalidatePath(path);
  }

  return NextResponse.json({ revalidated: true, paths, tags });
}
