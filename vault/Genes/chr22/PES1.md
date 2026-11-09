---
symbol: "PES1"
type: "gene"
col: 1847
ensembl_id: "ENSG00000100029"
name: "pescadillo ribosomal biogenesis factor 1"
location: "22q12.2"
module: 1
arm: "+"
pooled_cpm: 27.06
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PES1

*pescadillo ribosomal biogenesis factor 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.41× (z +15.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.791× (z -5.0, q 3e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF3D]] (+0.78, fdr 7e-06), [[PRMT5]] (+0.74, fdr 7e-06), [[SF3A3]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.41×** | +15.9 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +11.0 | 1e-25 | 33/47 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.41×** | +10.5 | 2e-23 | 36/47 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +10.0 | 2e-21 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.5 | 2e-19 | 33/43 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.61×** | +7.5 | 7e-12 | 32/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.3 | 3e-11 | 28/37 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +7.1 | 8e-11 | 31/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.0 | 1e-07 | 26/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.39×** | +5.4 | 4e-06 | 27/46 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.4 | 4e-06 | 2/48 (RKO, AN3 CA) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.3 | 5e-06 | 23/41 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 5e-06 | 29/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.0 | 2e-05 | 27/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.24×** | +4.8 | 6e-05 | 21/47 (NCI-H1573, PANC-1, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +4.7 | 8e-05 | 23/48 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.68×** | +4.4 | 3e-04 | 15/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.003 | 15/47 (NCI-H460, SW 900, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.004 | 16/48 (J82, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.007 | 13/48 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.009 | 14/46 (NCI-H1573, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.012 | 13/48 (NCI-H1792, NCI-H1573, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.012 | 18/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.030 | 9/48 (Hs 766T, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -5.0 | 3e-04 | 22/48 (A498, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.743×** | -4.9 | 3e-04 | 26/48 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -4.3 | 0.003 | 18/48 (HS-578T, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.003 | 24/48 (A498, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.013 | 18/46 (LS 180, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.646×** | -3.8 | 0.015 | 14/48 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.798×** | -3.7 | 0.015 | 10/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.015 | 15/48 (LS 180, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.800×** | -3.7 | 0.015 | 12/48 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.017 | 15/48 (KATO III, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -3.2 | 0.065 | 15/46 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.1 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.70× (z +9.8) | — |
| [[KATO III (line)]] | alt | 30.6 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 8.01× (z +9.4) | [[Digitoxin (drug)]] 0.5 µM 0.361× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 24.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.0) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.5× (z +10.0) | — |
| [[SW480 (line)]] | alt | 32.9 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.94× (z +10.2) | — |
| [[LoVo (line)]] | wt | 26.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.06× (z +10.1) | — |
| [[A498 (line)]] | wt | 43.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.3) |
| [[AN3 CA (line)]] | alt | 42.1 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0781× (z -11.1) |
| [[COLO 205 (line)]] | alt | 20.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 30.6× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 30.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 33.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.99× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 34.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.14× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.5 µM 0.0411× (z -9.5) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3D]] | +0.78 | +0.81 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PRMT5]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[SF3A3]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[NOL6]] | +0.72 | +0.76 / +0.62 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 860 |
| [[RRN3]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[MAK16]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 | STRING 994 |
| [[IMP4]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 968 |
| [[REXO4]] | +0.71 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[NOL8]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ZNF408]] | +0.70 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[PPAN]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 955 |
| [[BYSL]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 942 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers PES1's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.24× higher at baseline in the lines without RALGPS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.6, -2.9); signed map (-3.1, -42.9). **Vector** length 103, 24.9% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.57 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.8 | +15.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.4 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +10.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +4.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[8-Hydroxyquinoline (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | pescadillo ribosomal biogenesis factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,576,625-30,607,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PES, NOP7 |
| Gene groups (HGNC) | PeBoW complex |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O00541](https://www.uniprot.org/uniprotkb/O00541) (Pescadillo homolog):

> Component of the PeBoW complex, which is required for maturation of 28S and 5.8S ribosomal RNAs and formation of the 60S ribosome.

**Summary**, from NCBI Gene [23481](https://www.ncbi.nlm.nih.gov/gene/23481):

> This gene encodes a nuclear protein that contains a breast cancer associated gene 1 (BRCA1) C-terminal interaction domain. The encoded protein interacts with BOP1 and WDR12 to form the PeBoW complex, which plays a critical role in cell proliferation via pre-rRNA processing and 60S ribosomal subunit maturation. Expression of this gene may play an important role in breast cancer proliferation and tumorigenicity. Alternatively spliced transcript variants encoding multiple isoforms have been …

**Accessions** — [HGNC:8848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8848) · Entrez [23481](https://www.ncbi.nlm.nih.gov/gene/23481) · UniProt [O00541](https://www.uniprot.org/uniprotkb/O00541) · Ensembl [ENSG00000100029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100029)

## Data

Gene col 1847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1847); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1847]; `tensor/DDL_lfc|DDL_z.npy` [1847]; `embed/gene_vectors.npy` [1847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1847 or target_col == 1847). Every well: [[PES1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PES1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
