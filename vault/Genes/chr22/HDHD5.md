---
symbol: "HDHD5"
type: "gene"
col: 933
ensembl_id: "ENSG00000069998"
name: "haloacid dehalogenase like hydrolase domain containing 5"
location: "22q11.1"
module: 164
arm: "+"
pooled_cpm: 35.57
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# HDHD5

*haloacid dehalogenase like hydrolase domain containing 5* — 22q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.60× (z +4.6, q 0.002, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.474× (z -19.7, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMS19]] (+0.74, fdr 7e-06), [[CABIN1]] (+0.70, fdr 7e-06), [[YEATS2]] (+0.69, fdr 1e-05); moves opposite to [[PTPRK]] (-0.58, fdr 1e-05), [[ZNF655]] (-0.56, fdr 1e-05), [[RIPK2-DT]] (-0.56, fdr 3e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACE1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.6 | 0.002 | 19/46 (NCI-H2030, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +4.5 | 0.002 | 17/47 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.016 | 18/47 (A549, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.067 | 9/46 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.20× | +3.4 | 0.067 | 16/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.2 | 0.10 | 16/47 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.10 | 14/47 (SNU-423, HCT15, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.17 | 11/47 (SW 900, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.474×** | -19.7 | 0e+00 | 41/47 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.495×** | -12.6 | 4e-34 | 32/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -10.7 | 1e-24 | 33/42 (C32, SW48, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.597×** | -9.6 | 9e-20 | 28/44 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -7.6 | 2e-12 | 31/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -7.0 | 3e-10 | 29/45 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -6.2 | 5e-08 | 29/47 (HOP62, SNU-423, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.722×** | -6.1 | 1e-07 | 28/47 (C32, SW 1088, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -5.6 | 1e-06 | 19/38 (C32, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.789×** | -4.4 | 6e-04 | 21/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.797×** | -4.2 | 0.001 | 16/47 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.002 | 21/46 (hTERT-HPNE, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.861× | -3.9 | 0.004 | 17/47 (C32, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.821×** | -3.7 | 0.009 | 15/47 (C-33 A, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.009 | 15/47 (AN3 CA, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 100 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -43.5) |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0647× (z -14.8) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 48.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.8) |
| [[C-33 A (line)]] | alt | 108 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.7) |
| [[HS-578T (line)]] | alt | 61.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -21.9) |
| [[PANC-1 (line)]] | alt | 38.6 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.6) |
| [[RKO (line)]] | wt | 45.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -11.5) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -9.1) |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.9) |
| [[HCT15 (line)]] | alt | 56.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0695× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.3) |
| [[SW48 (line)]] | wt | 52.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.5) |
| [[A549 (line)]] | wt | 31.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -18.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 68.6 | 0 | 2 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0537× (z -9.9) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0974× (z -16.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.7) |
| [[J82 (line)]] | alt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.8) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.395× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS19]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[TRIT1]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TRMU]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[PEX3]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SLX9]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[RAB20]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.66 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[UBE2O]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PRMT7]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TFB1M]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[DDX5]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CHMP3]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | C | HACE1 activity raises HDHD5's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, -18.1); signed map (-38.9, 21.3). **Vector** length 117, 30.5% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -19.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.2 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | haloacid dehalogenase like hydrolase domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.1 — chr22:17,137,511-17,165,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CECR5 |
| Gene groups (HGNC) | Haloacid dehalogenase like hydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q9BXW7](https://www.uniprot.org/uniprotkb/Q9BXW7) carries no function annotation.

**Summary**, from NCBI Gene [27440](https://www.ncbi.nlm.nih.gov/gene/27440):

> Predicted to be involved in glycerophospholipid biosynthetic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1843) · Entrez [27440](https://www.ncbi.nlm.nih.gov/gene/27440) · UniProt [Q9BXW7](https://www.uniprot.org/uniprotkb/Q9BXW7) · Ensembl [ENSG00000069998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069998)

## Data

Gene col 933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 933); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 933]; `tensor/DDL_lfc|DDL_z.npy` [933]; `embed/gene_vectors.npy` [933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 933 or target_col == 933). Every well: [[HDHD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDHD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
