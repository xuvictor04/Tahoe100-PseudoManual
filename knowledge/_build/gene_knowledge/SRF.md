> [!summary] In one line
> SRF is a MADS-box transcription factor that sits on CArG-box promoters and delivers two different programmes — immediate-early genes or contractile and cytoskeletal genes — depending on which family of coactivators reaches it.

## What it is

SRF binds the CArG box, CC(A/T)₆GG, the core of the serum response element, through an N-terminal MADS box that also handles dimerisation. The factor is broadly expressed and largely constitutively bound at its targets; essentially all regulation happens one level up, at the coactivators. SRF is best understood as a switchboard with two incoming lines.

The first line is the ternary complex factors — ELK1, ELK4/SAP-1, ELK3/NET — recruited to SRF and activated by ERK phosphorylation. This is the growth-factor, immediate-early route: FOS, EGR1, JUNB. The second is the myocardin family — MRTFA/MKL1, MRTFB and MYOCD. These carry RPEL motifs that bind monomeric G-actin, which holds them cytoplasmic; Rho-driven actin polymerisation depletes the free G-actin pool, releases them into the nucleus and switches SRF onto cytoskeletal and contractile targets: ACTA2, ACTB, CNN1, TAGLN, vinculin. The two families compete for the same surface, so one factor reads either mitogenic signalling or the mechanical state of the cytoskeleton.

Srf-null mouse embryos fail gastrulation and never form mesoderm, with SRF-dependent immediate-early and α-actin genes unexpressed. Conditional deletion shows requirements across cardiac, smooth and skeletal muscle, and in neurons for activity-dependent transcription; in muscle it works alongside, not instead of, the myogenic bHLH and MEF2 machinery.

## Why it appears in this work

SRF is in this vault as a candidate native-tissue driver of [[MG53 (TRIM72)]], part of the muscle and promoter transcription-factor panel assembled alongside [[MEF2A]] and [[MYOD1]]. The question is upstream: if something sets TRIM72 transcription in these non-muscle lines, is it a recognisable myogenic regulator? SRF is also entangled with [[ELK4]], which appears prominently elsewhere in this analysis: ELK4 is one of SRF's own ternary complex factors, so the two share CArG-box targets and their inferred activities are not independent. A ranking placing both high reports overlapping evidence, not two converging lines. See [[Transcription factor activity inference]].

## What is uncertain

The reported myogenic control of the TRIM72 promoter runs through a MEF2 site and an adjacent E-box; no CArG element there has been characterised, and SRF is not listed as a TRIM72 regulator in the curated network used here. Its presence in this panel is a candidate choice justified by lineage logic, not a documented regulatory link; nothing here should be read as establishing one.

Two cautions matter. Because SRF is controlled at the coactivator level, its mRNA is a poor proxy for its activity — the argument for regulon-based inference, which has its own problem here: SRF's regulon is dominated by immediate-early genes, and those respond to almost any perturbation. An inferred "SRF activity" rising across a drug panel may be reporting generic stress rather than anything SRF-specific. Worse, the MRTF arm is driven by actin dynamics, so cytoskeleton-disrupting compounds activate SRF through a route unrelated to the biology under study — a real confound in a several-hundred-compound screen. Finally, SRF's role in cancer is context-dependent, so its activity carries no fixed directional meaning.

## References

- Arsenian et al., 1998, EMBO Journal — Srf-null mouse embryos show a severe gastrulation defect with impaired Egr-1, c-fos and α-actin expression, identifying SRF as essential for mesoderm formation.
- Miralles et al., 2003, Cell — actin dynamics control SRF activity through G-actin binding and nuclear accumulation of the coactivator MAL/MRTFA.
- Olson & Nordheim, 2010, Nature Reviews Molecular Cell Biology — review linking actin dynamics and SRF-dependent transcription to cell motility.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by synergism of MyoD (or myogenin) and MEF2 at a conserved MEF2 site adjacent to an E-box.
