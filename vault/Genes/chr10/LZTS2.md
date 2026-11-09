---
symbol: "LZTS2"
type: "gene"
col: 2883
ensembl_id: "ENSG00000107816"
name: "leucine zipper tumor suppressor 2"
location: "10q24.31"
module: 103
arm: "+"
pooled_cpm: 18.39
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 32
n_dd_up_clean: 5
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# LZTS2

*leucine zipper tumor suppressor 2* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[9-ING-41 (drug)]] 0.5 µM: 1.66× (z +4.0, q 0.033, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.156× (z -23.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFPT]] (+0.61, fdr 1e-05), [[SOX12]] (+0.61, fdr 7e-06), [[BRPF1]] (+0.60, fdr 3e-05); moves opposite to [[EFR3A]] (-0.60, fdr 3e-05), [[APPL2]] (-0.54, fdr 1e-04), [[GNG12]] (-0.52, fdr 9e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PAQR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.033 | 15/45 (SK-MEL-2, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.9 | 0.033 | 16/44 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.044 | 21/46 (MIA PaCa-2, LoVo, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.072 | 15/45 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.072 | 16/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.13 | 13/46 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.13 | 14/45 (RKO, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.48× | +3.1 | 0.13 | 5/47 (A498, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.13 | 12/45 (CHP-212, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.156×** | -23.9 | 0e+00 | 47/47 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.172×** | -22.6 | 0e+00 | 46/47 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.296×** | -22.1 | 0e+00 | 42/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.239×** | -18.4 | 0e+00 | 44/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.316×** | -14.2 | 6e-44 | 42/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -12.3 | 8e-33 | 43/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -12.3 | 1e-32 | 42/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -12.2 | 1e-32 | 35/45 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.423×** | -11.0 | 1e-26 | 42/46 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -9.9 | 2e-21 | 37/45 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.614×** | -8.8 | 5e-17 | 38/47 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.508×** | -8.7 | 2e-16 | 38/46 (C-33 A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -8.1 | 2e-14 | 37/47 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.582×** | -6.9 | 2e-10 | 32/46 (NCI-H1792, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.593×** | -6.7 | 8e-10 | 32/47 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.331×** | -5.5 | 2e-06 | 28/47 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 19.0 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0730× (z -14.9) |
| [[C32 (line)]] | wt | 44.6 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0437× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.5) |
| [[A-172 (line)]] | wt | 61.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -26.7) |
| [[Hs 766T (line)]] | wt | 26.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0644× (z -17.6) |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -18.4) |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -16.0) |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 20.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.266× (z -11.1) |
| [[SW480 (line)]] | alt | 16.7 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0610× (z -23.5) |
| [[A549 (line)]] | wt | 10.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 11.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.6) |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.0) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.7) |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0618× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0628× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0773× (z -15.3) |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.168× (z -9.9) |
| [[H4 (line)]] | wt | 23.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0815× (z -10.5) |
| [[J82 (line)]] | alt | 11.1 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0913× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0743× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.0) |
| [[RKO (line)]] | wt | 17.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.1) |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0980× (z -13.7) |
| [[A-427 (line)]] | wt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -10.7) |
| [[A498 (line)]] | wt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.0) |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0659× (z -12.6) |
| [[KATO III (line)]] | alt | 10.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -9.7) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0942× (z -11.1) |
| [[LS 180 (line)]] | wt | 7.87 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0980× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.4) |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0736× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.8) |
| [[SW48 (line)]] | wt | 17.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.115× (z -8.9) |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFPT]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SOX12]] | +0.61 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[BRPF1]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[ZNF8-DT]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TMEM134]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ZNF446]] | +0.58 | +0.25 / +0.63 | both halves | 4e-04 |  |
| [[ABCB6]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TRADD]] | +0.56 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[TEX264]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FBXL15]] | +0.55 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[DDX41]] | +0.55 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[C1orf35]] | +0.54 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | -0.60 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[APPL2]] | -0.54 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[GNG12]] | -0.52 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[ACSL4]] | -0.49 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[TUSC3]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ARHGAP18]] | -0.48 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[REEP3]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[BCAP29]] | -0.48 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[SPCS3]] | -0.48 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[AIG1]] | -0.47 | -0.24 / -0.55 | both halves | 4e-04 |  |
| [[MRPL42]] | -0.47 | -0.30 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR7]] | B | PAQR7 activity raises LZTS2's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without PAQR7 | 0.058 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.0, -11.9); signed map (-30.1, 29.6). **Vector** length 72.8, 17.0% of its response variance represented; |z| ≥ 3 in 1,188 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.5 | -2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | -3.1 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -11.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper tumor suppressor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,996,618-101,007,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1813, LAPSER1 |
| Gene groups (HGNC) | Leucine zipper tumor suppressor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRK4](https://www.uniprot.org/uniprotkb/Q9BRK4) (Leucine zipper putative tumor suppressor 2):

> Negative regulator of katanin-mediated microtubule severing and release from the centrosome. Required for central spindle formation and the completion of cytokinesis. May negatively regulate axonal outgrowth by preventing the formation of microtubule bundles that are necessary for transport within the elongating axon. Negative regulator of the Wnt signaling pathway. Represses beta-catenin-mediated transcriptional activation by promoting the nuclear exclusion of beta-catenin.

**Summary**, from NCBI Gene [84445](https://www.ncbi.nlm.nih.gov/gene/84445):

> The protein encoded by this gene belongs to the leucine zipper tumor suppressor family of proteins, which function in transcription regulation and cell cycle control. This family member can repress beta-catenin-mediated transcriptional activation and is a negative regulator of the Wnt signaling pathway. It negatively regulates microtubule severing at centrosomes, and is necessary for central spindle formation and cytokinesis completion. It is implicated in cancer, where it may inhibit cell …

**Accessions** — [HGNC:29381](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29381) · Entrez [84445](https://www.ncbi.nlm.nih.gov/gene/84445) · UniProt [Q9BRK4](https://www.uniprot.org/uniprotkb/Q9BRK4) · Ensembl [ENSG00000107816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107816)

## Data

Gene col 2883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2883); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2883]; `tensor/DDL_lfc|DDL_z.npy` [2883]; `embed/gene_vectors.npy` [2883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2883 or target_col == 2883). Every well: [[LZTS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LZTS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
