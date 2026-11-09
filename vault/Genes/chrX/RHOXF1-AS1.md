---
symbol: "RHOXF1-AS1"
type: "gene"
col: 15112
ensembl_id: "ENSG00000258545"
name: "RHOXF1 antisense RNA 1"
location: "Xq24"
module: 27
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# RHOXF1-AS1

*RHOXF1 antisense RNA 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.86× (z +10.8, q 3e-24, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +7.6, q 7e-12, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.514× (z -5.5, q 2e-05, down in 17 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.598× (z -4.2, q 0.006, down in 13 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.226×, SW480 0.306×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0834×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0859×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.173×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HEC-1-A 0.224×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F10]] (+0.69, fdr 7e-06), [[JAKMIP2-AS1]] (+0.66, fdr 7e-06), [[APCDD1]] (+0.65, fdr 7e-06); moves opposite to [[PITPNC1]] (-0.49, fdr 4e-05), [[S100A16]] (-0.44, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERPINF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +10.8 | 3e-24 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +9.1 | 2e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.6 | 7e-12 | 6/18 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.2 | 1e-10 | 1/8 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.84×** | +4.9 | 1e-04 | 6/13 (SW480, KATO III, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.1 | 0.003 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.003 | 9/26 (HOP62, SW480, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.0 | 0.005 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.005 | 3/31 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.6 | 0.014 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.6 | 0.014 | 1/16 (HT-29) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.79×** | +3.5 | 0.026 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.037 | 4/25 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.039 | 1/12 (BT-474) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.090 | 2/37 (A-427, SNU-423) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HEC-1-A 0.226×, SW480 0.306×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 0.0834×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0859×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.173×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HEC-1-A 0.224×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.514×** | -5.5 | 2e-05 | 17/40 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -4.2 | 0.006 | 13/32 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Asciminib (drug)]] 0.5 µM |  | **0.626×** | -3.9 | 0.021 | 8/37 (SW1417, J82, …) | inconsistent across doses |  |
| [[Econazole (drug)]] 0.5 µM |  | 0.674× | -3.3 | 0.16 | 3/40 (SHP-77, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.13 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0834× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0859× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 16.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.224× (z -8.5) |
| [[SNU-423 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0576× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.667 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.554 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.830 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.534 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.875 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.813 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.915 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.752 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.630 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.773 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.539 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.844 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.907 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.697 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.605 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.574 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.558 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.709 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.873 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F10]] | +0.69 | +0.69 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[JAKMIP2-AS1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 | same gene group |
| [[APCDD1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GPR143]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[B3GAT1-DT]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[LINC02940]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TMEM139]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PSD2]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[NIHCOLE]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PKHD1]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNC1]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[S100A16]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINF1]] | B | SERPINF1 activity raises RHOXF1-AS1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without SERPINF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[FGD5]] | B | FGD5 activity raises RHOXF1-AS1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 1.36× lower at baseline in the lines without FGD5 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[F10]] | B | F10 activity raises RHOXF1-AS1's level | lines that do not express F10 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without F10 | 0.066 | ⚠ within organs, on part of the lines; also absent: SELENOP, NIHCOLE, NOTUM; maybe low, not absent |
| [[LINC00992]] | B | LINC00992 activity raises RHOXF1-AS1's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without LINC00992 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 43.9); signed map (62.0, 15.8). **Vector** length 39.0, 5.02% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +10.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +9.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +4.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +0.9 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.7 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | RHOXF1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq24 — chrX:120,036,236-120,146,855 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51582) · Entrez [101928969](https://www.ncbi.nlm.nih.gov/gene/101928969) · Ensembl [ENSG00000258545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258545)

## Data

Gene col 15112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15112); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15112]; `tensor/DDL_lfc|DDL_z.npy` [15112]; `embed/gene_vectors.npy` [15112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15112 or target_col == 15112). Every well: [[RHOXF1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOXF1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
