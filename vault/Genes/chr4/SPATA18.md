---
symbol: "SPATA18"
type: "gene"
col: 8627
ensembl_id: "ENSG00000163071"
name: "spermatogenesis associated 18"
location: "4q12"
module: 62
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# SPATA18

*spermatogenesis associated 18* — 4q12

> [!summary] In one line
> SPATA18 encodes Mieap, a p53-inducible mitochondrial protein proposed to run a form of mitochondrial quality control distinct from canonical mitophagy — a well-supported p53 target whose mechanism rests almost entirely on one laboratory's work.

## What it is

Two names, one gene. HGNC calls it SPATA18, "spermatogenesis associated 18"; the functional literature calls it Mieap, "mitochondria-eating protein". The protein is roughly 540 residues, associates with the mitochondrial outer membrane and binds cardiolipin.

The p53 connection is the best-established part: p53 binds a response element at the locus and induces the transcript — the basis on which the gene was characterised at all. On oxidative stress it was reported to drive one of two outcomes by severity — MALM, in which lysosomal proteins are delivered into the mitochondrial interior to degrade oxidised proteins and so "repair" the organelle, requiring BNIP3 and NIX; or, when repair fails, Mieap-induced vacuoles that engulf whole mitochondria.

That model has since been substantially revised by the same group: more recent work describes Mieap forming membrane-less organelles — condensates — involved in cardiolipin metabolism, a different kind of claim from lysosome-like compartments inside mitochondria. The cancer argument is that the axis is lost in tumours: reported inactivated in a large majority of primary colorectal cancers through p53 mutation or MIEAP and BNIP3 promoter methylation; Mieap-deficient mice show increased intestinal tumour burden. Expression is tissue-enhanced rather than ubiquitous, concentrated in fallopian tube and testis; in cultured cancer lines it is generally a low-abundance transcript.

## What is uncertain

Nearly all of the mechanism comes from one group, and independent replication of the central cell-biological claims is thin. MALM and Mieap-induced vacuoles are not standard entities elsewhere in the mitochondrial quality-control field, and the originating laboratory has itself moved from that model toward cardiolipin-handling condensates, so the earlier account should not be quoted as settled. How any of this relates to PINK1/Parkin mitophagy is unmapped.

What survives best is the transcriptional fact: SPATA18 is p53-responsive. Beyond that, two tensions deserve stating. The expression pattern — ciliated epithelium and germ line — sits awkwardly with a general p53-controlled quality-control function in all tissues. And the tumour-suppressor case rests on promoter-methylation frequencies in modest cohorts plus a mouse model, which supports an association more firmly than it supports the proposed mechanism being the reason. The gene name is also a hazard: "spermatogenesis associated" reflects cataloguing history, not a demonstrated reproductive role.

## References

- Kitamura et al., 2011, PLoS ONE — identified Mieap as a p53-inducible protein controlling mitochondrial quality by repairing or eliminating unhealthy mitochondria.
- Tsuneki et al., 2015, Scientific Reports — Mieap suppresses murine intestinal tumour formation via its mitochondrial quality control function.
- Kamino et al., 2016, Oncogenesis — Mieap-regulated mitochondrial quality control is frequently inactivated in human colorectal cancer.
- Nakamura & Arakawa, 2017, Cancer Science — review framing Mieap-regulated mitochondrial quality control as a function of p53.
- Ikari et al., 2024, iScience — Mieap forms membrane-less organelles involved in cardiolipin metabolism, revising the earlier mechanistic model.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.08× (z +17.8, q 0e+00, up in 11 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.0732×, NCI-H460 0.0895×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.126×, LS 180 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0881×; ⚠ toxic); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.122×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LS 180 0.200×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTA2]] (+0.87, fdr 7e-06), [[ZMAT3]] (+0.83, fdr 7e-06), [[PINCR]] (+0.83, fdr 7e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[RETSAT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.08×** | +17.8 | 0e+00 | 11/15 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +10.3 | 2e-22 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.68×** | +9.7 | 6e-20 | 7/15 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +8.6 | 9e-16 | 7/16 (NCI-H460, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +8.3 | 1e-14 | 12/18 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +8.2 | 2e-14 | 3/7 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +7.4 | 1e-11 | 11/20 (LoVo, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.1 | 1e-10 | 7/19 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +6.8 | 8e-10 | 2/4 (A498, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +5.4 | 5e-06 | 9/19 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +4.9 | 5e-05 | 11/15 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.54×** | +4.7 | 1e-04 | 9/19 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +4.6 | 2e-04 | 1/9 (NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.4 | 4e-04 | 5/8 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.94×** | +4.4 | 5e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.029 | 5/20 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.57×** | +3.2 | 0.035 | 0/10 | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +2.9 | 0.081 | 6/18 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8627.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (LoVo 0.0732×, NCI-H460 0.0895×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.126×, LS 180 0.180×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0881×; ⚠ toxic); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.122×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (LS 180 0.200×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.664× | -3.1 | 0.36 | 3/19 (HT-29, HCT15, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | 0.666× | -3.1 | 0.36 | 3/19 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.05 µM |  | 0.653× | -3.0 | 0.36 | 2/20 (NCI-H2347, LS 180) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.675× | -3.0 | 0.36 | 3/20 (LS 180, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.7 | 2 | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.78× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.0732× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 2.91 | 2 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.0895× (z -9.0) |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -8.7) |
| [[A498 (line)]] | wt | 14.8 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.04× (z +9.6) | — |
| [[KATO III (line)]] | alt | 3.78 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0608× (z -8.6) |
| [[A-172 (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.512 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTA2]] | +0.87 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[ZMAT3]] | +0.83 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PINCR]] | +0.83 | +0.70 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[FAS]] | +0.79 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ABCA12]] | +0.78 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[MDM2]] | +0.77 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[PTCHD4]] | +0.74 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[BAX]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.72 | +0.35 / +0.77 | both halves | 1e-04 |  |
| [[GRIN2C]] | +0.71 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[PURPL]] | +0.71 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[TP53I3]] | +0.71 | +0.57 / +0.64 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPATA18's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SULF2]] | C | SULF2 activity raises SPATA18's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without SULF2 | 0.059 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RETSAT]] | B | SPATA18 activity raises RETSAT's level | lines that do not express SPATA18 (26) vs lines expressing it (24) | 1.34× lower at baseline in the lines without SPATA18 | 0.079 | ⚠ within organs, on part of the lines; also absent: GPRIN2, MUC5AC, SIDT1 |
| [[PLXNB2]] | B | SPATA18 activity raises PLXNB2's level | lines that do not express SPATA18 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without SPATA18 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRIN2, MUC5AC, SIDT1 |
| [[SULF2]] | C | SPATA18 activity raises SULF2's level | lines that do not express SPATA18 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without SPATA18 | 0.099 | ⚠ within organs, on part of the lines; also absent: GPRIN2, MUC5AC, SIDT1; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.889). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.4, 36.5); signed map (42.4, -23.3). **Vector** length 53.5, 13.4% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.59 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.66 to 6); *apoptosis* (hallmark, mean cos +0.62 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.8 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:52,051,304-52,097,299 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32906 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC71](https://www.uniprot.org/uniprotkb/Q8TC71) (Mitochondria-eating protein):

> Key regulator of mitochondrial quality that mediates the repairing or degradation of unhealthy mitochondria in response to mitochondrial damage. Mediator of mitochondrial protein catabolic process (also named MALM) by mediating the degradation of damaged proteins inside mitochondria by promoting the accumulation in the mitochondrial matrix of hydrolases that are characteristic of the lysosomal lumen. Also involved in mitochondrion degradation of damaged mitochondria by promoting the formation …

**Summary**, from NCBI Gene [132671](https://www.ncbi.nlm.nih.gov/gene/132671):

> This gene encodes a p53-inducible protein that is able to induce lysosome-like organelles within mitochondria that eliminate oxidized mitochondrial proteins, thereby contributing to mitochondrial quality control. Dysregulation of mitochondrial quality control is associated with cancer and degenerative diseases. The encoded protein mediates accumulation of the lysosome-like mitochondrial organelles through interaction with B cell lymphoma 2 interacting protein 3 and B cell lymphoma 2 interacting …

**Accessions** — [HGNC:29579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29579) · Entrez [132671](https://www.ncbi.nlm.nih.gov/gene/132671) · UniProt [Q8TC71](https://www.uniprot.org/uniprotkb/Q8TC71) · Ensembl [ENSG00000163071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163071)

## Data

Gene col 8627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8627); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8627]; `tensor/DDL_lfc|DDL_z.npy` [8627]; `embed/gene_vectors.npy` [8627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8627 or target_col == 8627). Every well: [[SPATA18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SPATA18.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
