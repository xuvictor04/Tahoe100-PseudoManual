---
symbol: "EPM2AIP1"
type: "gene"
col: 10937
ensembl_id: "ENSG00000178567"
name: "EPM2A interacting protein 1"
location: "3p22.2"
module: 21
arm: "+"
pooled_cpm: 20.96
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EPM2AIP1

*EPM2A interacting protein 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +12.5, q 5e-33, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.920× (z -5.3, q 7e-05, down in 1 of 45 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.285×, A-427 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.149×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.123×; ⚠ toxic; cell-cycle shift, explains ~12% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING4]] (+0.67, fdr 1e-05), [[DNAJC30]] (+0.64, fdr 1e-05), [[UBOX5-AS1]] (+0.63, fdr 1e-05); moves opposite to [[EFR3A]] (-0.55, fdr 2e-05), [[SMC6]] (-0.53, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[MTERF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +12.5 | 5e-33 | 35/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +11.4 | 2e-27 | 42/45 (HEC-1-A, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +9.6 | 2e-19 | 35/45 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +8.2 | 3e-14 | 24/39 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +8.0 | 1e-13 | 26/45 (HEC-1-A, SK-MEL-2, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +7.8 | 7e-13 | 33/45 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.3 | 2e-11 | 27/45 (HEC-1-A, SW1417, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.1 | 8e-11 | 22/45 (A-172, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.9 | 4e-10 | 27/44 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.7 | 1e-09 | 23/45 (J82, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +6.0 | 1e-07 | 22/45 (A-172, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.2 | 1e-05 | 20/44 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +4.0 | 0.003 | 14/45 (SK-MEL-2, SW1417, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.24×** | +3.9 | 0.005 | 12/32 (LoVo, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.007 | 10/45 (PANC-1, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.014 | 9/45 (PANC-1, A-172, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 0.285×, A-427 0.334×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.149×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.123×; ⚠ toxic; cell-cycle shift, explains ~12% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -5.3 | 7e-05 | 1/45 (NCI-H2347) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.821×** | -3.7 | 0.070 | 14/44 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.2 | 0.25 | 11/45 (C32, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.90× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 18.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.0) | — |
| [[LoVo (line)]] | wt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING4]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[DNAJC30]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.63 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SEM1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[APPBP2]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PEX6]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.59 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[RPL34-DT]] | +0.59 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ZRANB2-AS1]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[PCF11-AS1]] | +0.59 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[FAM184B]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MYL6B]] | +0.59 | +0.37 / +0.52 | both halves | 7e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SMC6]] | -0.53 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPM2AIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTERF1]] | C | EPM2AIP1 activity raises MTERF1's level | lines that do not express EPM2AIP1 (3) vs lines expressing it (47) | 4.72× lower at baseline in the lines without EPM2AIP1 | 0.022 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |
| [[PSMC2]] | C | EPM2AIP1 activity lowers PSMC2's level | lines that do not express EPM2AIP1 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without EPM2AIP1 | 0.092 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MLF1, ADAL, TTC30A |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, 26.7); signed map (-4.4, -2.7). **Vector** length 76.9, 14.2% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +11.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +7.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | -2.1 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | EPM2A interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:36,985,043-36,993,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0766, FLJ11207 |
| Matched by | ensembl_id |

UniProt [Q7L775](https://www.uniprot.org/uniprotkb/Q7L775) carries no function annotation.

**Summary**, from NCBI Gene [9852](https://www.ncbi.nlm.nih.gov/gene/9852):

> The EPM2A gene, which encodes laforin, is mutated in an autosomal recessive form of adolescent progressive myoclonus epilepsy. The protein encoded by this gene binds to laforin, but its function is not known. This gene is intronless. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:19735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19735) · Entrez [9852](https://www.ncbi.nlm.nih.gov/gene/9852) · UniProt [Q7L775](https://www.uniprot.org/uniprotkb/Q7L775) · Ensembl [ENSG00000178567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178567)

## Data

Gene col 10937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10937); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10937]; `tensor/DDL_lfc|DDL_z.npy` [10937]; `embed/gene_vectors.npy` [10937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10937 or target_col == 10937). Every well: [[EPM2AIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPM2AIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
