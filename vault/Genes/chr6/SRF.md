---
symbol: "SRF"
type: "gene"
col: 3390
ensembl_id: "ENSG00000112658"
name: "serum response factor"
location: "6p21.1"
module: 138
arm: "+"
pooled_cpm: 26.29
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138", "written"]
generated_by: "tahoemap"
---

# SRF

*serum response factor* — 6p21.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SRF is a MADS-box transcription factor that sits on CArG-box promoters and delivers two different programmes — immediate-early genes or contractile and cytoskeletal genes — depending on which family of coactivators reaches it.

## What it is

SRF binds the CArG box, CC(A/T)₆GG, the core of the serum response element, through an N-terminal MADS box that also handles dimerisation. The factor is broadly expressed and largely constitutively bound at its targets; essentially all regulation happens one level up, at the coactivators. SRF is best understood as a switchboard with two incoming lines.

The first line is the ternary complex factors — ELK1, ELK4/SAP-1, ELK3/NET — recruited to SRF and activated by ERK phosphorylation. This is the growth-factor, immediate-early route: FOS, EGR1, JUNB. The second is the myocardin family — MRTFA/MKL1, MRTFB and MYOCD. These carry RPEL motifs that bind monomeric G-actin, which holds them cytoplasmic; Rho-driven actin polymerisation depletes the free G-actin pool, releases them into the nucleus and switches SRF onto cytoskeletal and contractile targets: ACTA2, ACTB, CNN1, TAGLN, vinculin. The two families compete for the same surface, so one factor reads either mitogenic signalling or the mechanical state of the cytoskeleton.

Srf-null mouse embryos fail gastrulation and never form mesoderm, with SRF-dependent immediate-early and α-actin genes unexpressed. Conditional deletion shows requirements across cardiac, smooth and skeletal muscle, and in neurons for activity-dependent transcription; in muscle it works alongside, not instead of, the myogenic bHLH and MEF2 machinery.

## What is uncertain

SRF is often grouped with the muscle factors, but the reported myogenic control of the TRIM72 promoter runs through a MEF2 site and an adjacent E-box; no CArG element there has been characterised, so that grouping is lineage logic, not a documented regulatory link.

Two cautions matter. Because SRF is controlled at the coactivator level, its mRNA is a poor proxy for its activity — the argument for regulon-based inference, which has its own problem here: SRF's regulon is dominated by immediate-early genes, and those respond to almost any perturbation. An inferred "SRF activity" rising across a drug panel may be reporting generic stress rather than anything SRF-specific. Worse, the MRTF arm is driven by actin dynamics, so cytoskeleton-disrupting compounds activate SRF through a route unrelated to the biology under study — a real confound in a several-hundred-compound screen. Finally, SRF's role in cancer is context-dependent, so its activity carries no fixed directional meaning.

## References

- Arsenian et al., 1998, EMBO Journal — Srf-null mouse embryos show a severe gastrulation defect with impaired Egr-1, c-fos and α-actin expression, identifying SRF as essential for mesoderm formation.
- Miralles et al., 2003, Cell — actin dynamics control SRF activity through G-actin binding and nuclear accumulation of the coactivator MAL/MRTFA.
- Olson & Nordheim, 2010, Nature Reviews Molecular Cell Biology — review linking actin dynamics and SRF-dependent transcription to cell motility.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — TRIM72 is transcriptionally activated by synergism of MyoD (or myogenin) and MEF2 at a conserved MEF2 site adjacent to an E-box.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +13.0, q 4e-36, up in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.17× (z +3.3, q 0.051, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.700× (z -5.2, q 1e-04, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZYX]] (+0.59, fdr 1e-05), [[LRCH4]] (+0.56, fdr 1e-05), [[CLPTM1L]] (+0.55, fdr 1e-05); moves opposite to [[VPS29]] (-0.52, fdr 3e-05), [[RPL39]] (-0.49, fdr 6e-05), [[RAB18]] (-0.49, fdr 1e-04).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.85×** | +13.0 | 4e-36 | 35/47 (AsPC-1, HT-29, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.54×** | +6.5 | 2e-08 | 29/46 (LS 180, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +5.8 | 1e-06 | 28/48 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +5.4 | 1e-05 | 28/47 (LS 180, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.42×** | +5.0 | 5e-05 | 22/39 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +4.8 | 1e-04 | 25/47 (LS 180, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +4.7 | 2e-04 | 24/47 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.9 | 0.007 | 18/46 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.7 | 0.013 | 15/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.051 | 16/48 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.051 | 15/47 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.055 | 9/46 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.055 | 13/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.060 | 11/46 (LoVo, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.0 | 0.089 | 13/47 (KATO III, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.700×** | -5.2 | 1e-04 | 26/47 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.714×** | -4.9 | 2e-04 | 24/47 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.781×** | -3.8 | 0.031 | 22/47 (RKO, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.775×** | -3.6 | 0.042 | 19/48 (H4, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.803×** | -3.4 | 0.090 | 17/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.809× | -3.2 | 0.11 | 20/48 (LOX-IMVI, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 49.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.6 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[A549 (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.111× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 22.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.168× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.216× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +8.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-1 (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZYX]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LRCH4]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CLPTM1L]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GSE1]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[STK11]] | +0.53 | +0.67 / +0.32 | both halves | 2e-04 |  |
| [[AJUBA]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ERF]] | +0.52 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[TRIM28]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[CELSR3]] | +0.52 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[KMT2B]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TAOK2]] | +0.51 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[MUS81]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS29]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[RPL39]] | -0.49 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[RAB18]] | -0.49 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[MIGA1]] | -0.47 | -0.55 / -0.32 | both halves | 1e-04 |  |
| [[ACP1]] | -0.47 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[PIK3C3]] | -0.47 | -0.59 / -0.40 | both halves | 5e-05 | pathway: RHO GTPase Effectors |
| [[LONP2]] | -0.47 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[VIPAS39]] | -0.47 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[GSTO1]] | -0.46 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[CMAS]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[ORC3]] | -0.46 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[ARPC1A]] | -0.46 | -0.54 / -0.38 | both halves | 6e-05 | pathway: RHO GTPase Effectors |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.9, -25.1); signed map (4.5, -6.0). **Vector** length 92.0, 21.0% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.9 | +13.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.4 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.8 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.8 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | serum response factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,171,269-43,181,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCM1 |
| Gene groups (HGNC) | MADS box family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 17 pathways, smallest: Regulation of NPAS4 gene transcription; Regulation of NPAS4 gene expression; Cardiogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P11831](https://www.uniprot.org/uniprotkb/P11831) (Serum response factor):

> SRF is a transcription factor that binds to the serum response element (SRE), a short sequence of dyad symmetry located 300 bp to the 5' of the site of transcription initiation of some genes (such as FOS). Together with MRTFA transcription coactivator, controls expression of genes regulating the cytoskeleton during development, morphogenesis and cell migration. The SRF-MRTFA complex activity responds to Rho GTPase-induced changes in cellular globular actin (G-actin) concentration, thereby …

**Summary**, from NCBI Gene [6722](https://www.ncbi.nlm.nih.gov/gene/6722):

> This gene encodes a ubiquitous nuclear protein that stimulates both cell proliferation and differentiation. It is a member of the MADS (MCM1, Agamous, Deficiens, and SRF) box superfamily of transcription factors. This protein binds to the serum response element (SRE) in the promoter region of target genes. This protein regulates the activity of many immediate-early genes, for example c-fos, and thereby participates in cell cycle regulation, apoptosis, cell growth, and cell differentiation. This …

**Accessions** — [HGNC:11291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11291) · Entrez [6722](https://www.ncbi.nlm.nih.gov/gene/6722) · UniProt [P11831](https://www.uniprot.org/uniprotkb/P11831) · Ensembl [ENSG00000112658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112658)

## Data

Gene col 3390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3390); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3390]; `tensor/DDL_lfc|DDL_z.npy` [3390]; `embed/gene_vectors.npy` [3390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3390 or target_col == 3390). Every well: [[SRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SRF.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
