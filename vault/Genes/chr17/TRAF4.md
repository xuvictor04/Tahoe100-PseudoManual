---
symbol: "TRAF4"
type: "gene"
col: 1156
ensembl_id: "ENSG00000076604"
name: "TNF receptor associated factor 4"
location: "17q11.2"
module: 14
arm: "+"
pooled_cpm: 14.79
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TRAF4

*TNF receptor associated factor 4* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.60× (z +19.9, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.738× (z -6.3, q 1e-07, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42EP1]] (+0.64, fdr 7e-06), [[NFKBIE]] (+0.63, fdr 1e-05), [[PIM3]] (+0.61, fdr 1e-05); moves opposite to [[ATP2C1]] (-0.50, fdr 3e-05), [[PIGN]] (-0.50, fdr 3e-05), [[STRAP]] (-0.49, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CGN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +19.9 | 0e+00 | 41/45 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.09×** | +16.0 | 0e+00 | 40/46 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +10.9 | 2e-25 | 31/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +9.8 | 2e-20 | 37/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.4 | 6e-15 | 26/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.2 | 5e-08 | 28/41 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 5e-08 | 24/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.48×** | +5.8 | 4e-07 | 29/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.48×** | +5.7 | 6e-07 | 28/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.41×** | +5.0 | 3e-05 | 21/47 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.40×** | +5.0 | 4e-05 | 18/41 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 6e-05 | 20/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.38×** | +4.7 | 9e-05 | 19/46 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.023 | 11/47 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.024 | 7/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cytarabine (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.028 | 8/46 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.067 | 5/40 (COLO 205, A-427, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -6.3 | 1e-07 | 24/46 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.757×** | -3.9 | 0.029 | 17/45 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.842× | -3.5 | 0.086 | 13/48 (SW480, Hs 766T, …) | all doses, flat | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | **0.833×** | -3.4 | 0.086 | 7/48 (NCI-H460, C-33 A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.098 | 2/48 (A-427, SW1417) | inconsistent across doses | position effect removed |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.813× | -3.1 | 0.21 | 8/47 (A498, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +13.5) | — |
| [[A-172 (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -9.8) |
| [[J82 (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.05 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +9.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.119× (z -9.5) |
| [[SW1417 (line)]] | alt | 19.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.7) |
| [[A498 (line)]] | wt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 7.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 9.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -10.8) |
| [[KATO III (line)]] | alt | 23.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP1]] | +0.64 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PIM3]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PRR14]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NGFR]] | +0.59 | +0.46 / +0.66 | both halves | 3e-05 | STRING 746 |
| [[TPPP]] | +0.57 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PLXNB2]] | +0.57 | +0.71 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[GRINA]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PBX2]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[BCL3]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[TNFRSF14]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[RHOV]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2C1]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PIGN]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[STRAP]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[KPNB1]] | -0.49 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[MTPN]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[MFN1]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[HACD3]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NBAS]] | -0.48 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[STMP1]] | -0.47 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[PDIA3]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TDP1]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[GDAP2]] | -0.47 | -0.39 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGN]] | B | CGN activity raises TRAF4's level | lines that do not express CGN (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without CGN | 0.006 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[PCDH1]] | B | PCDH1 activity raises TRAF4's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without PCDH1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[CRB3]] | B | CRB3 activity raises TRAF4's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CRB3 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[EPPK1]] | B | EPPK1 activity raises TRAF4's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.43× lower at baseline in the lines without EPPK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[TRIM15]] | B | TRIM15 activity raises TRAF4's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without TRIM15 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[ANO9]] | B | ANO9 activity raises TRAF4's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.37× lower at baseline in the lines without ANO9 | 0.075 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[RHOV]] | B | RHOV activity raises TRAF4's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without RHOV | 0.087 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.7, 33.2); signed map (12.6, -17.1). **Vector** length 92.9, 19.9% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +19.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +8.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | -0.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,744,011-28,750,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CART1, MLN62, RNF83 |
| Gene groups (HGNC) | Ring finger proteins; TNF receptor associated factors; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUZ4](https://www.uniprot.org/uniprotkb/Q9BUZ4) (TNF receptor-associated factor 4):

> Adapter protein with E3 ligase activity that is involved in many diverse biological processes including cell proliferation, migration, differentiation, DNA repair, platelet activation or apoptosis. Promotes EGFR-mediated signaling by facilitating the dimerization of EGFR and downstream AKT activation thereby promoting cell proliferation. Ubiquitinates SMURF2 through 'Lys-48'-linked ubiquitin chain leading to SMURF2 degradation through the proteasome and subsequently osteogenic differentiation. …

**Summary**, from NCBI Gene [9618](https://www.ncbi.nlm.nih.gov/gene/9618):

> This gene encodes a member of the TNF receptor associated factor (TRAF) family. TRAF proteins are associated with, and mediate signal transduction from members of the TNF receptor superfamily. The encoded protein has been shown to interact with neurotrophin receptor, p75 (NTR/NTSR1), and negatively regulate NTR induced cell death and NF-kappa B activation. This protein has been found to bind to p47phox, a cytosolic regulatory factor included in a multi-protein complex known as NAD(P)H oxidase. …

**Accessions** — [HGNC:12034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12034) · Entrez [9618](https://www.ncbi.nlm.nih.gov/gene/9618) · UniProt [Q9BUZ4](https://www.uniprot.org/uniprotkb/Q9BUZ4) · Ensembl [ENSG00000076604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076604)

## Data

Gene col 1156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1156); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1156]; `tensor/DDL_lfc|DDL_z.npy` [1156]; `embed/gene_vectors.npy` [1156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1156 or target_col == 1156). Every well: [[TRAF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
