---
symbol: "RIC8A"
type: "gene"
col: 10882
ensembl_id: "ENSG00000177963"
name: "RIC8 guanine nucleotide exchange factor A"
location: "11p15.5"
module: 2
arm: "+"
pooled_cpm: 24.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RIC8A

*RIC8 guanine nucleotide exchange factor A* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.54× (z +8.0, q 9e-13, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.546× (z -15.9, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1AD]] (+0.72, fdr 7e-06), [[MAPK7]] (+0.68, fdr 7e-06), [[CPTP]] (+0.66, fdr 7e-06); moves opposite to [[PNISR]] (-0.57, fdr 8e-05), [[CYB5D2]] (-0.52, fdr 3e-05), [[KPNA5]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +8.0 | 9e-13 | 31/47 (HT-29, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.6 | 0.001 | 22/44 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +4.1 | 0.007 | 15/47 (Hs 766T, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +3.7 | 0.026 | 11/46 (HEC-1-A, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.22×** | +3.6 | 0.033 | 14/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.21×** | +3.5 | 0.041 | 17/48 (SW480, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.041 | 13/46 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.20×** | +3.4 | 0.055 | 10/47 (SW480, HT-29, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.057 | 7/47 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.072 | 10/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.0 | 0.12 | 9/47 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.12 | 5/48 (RPMI-7951, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -15.9 | 0e+00 | 38/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -10.2 | 9e-22 | 33/47 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -9.1 | 2e-17 | 32/47 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -8.9 | 8e-17 | 33/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -8.5 | 2e-15 | 25/47 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -7.2 | 6e-11 | 25/47 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.743×** | -5.5 | 2e-06 | 22/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.776×** | -4.6 | 4e-04 | 22/47 (A-427, SNU-423, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.789×** | -4.4 | 6e-04 | 16/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.821×** | -3.7 | 0.013 | 18/47 (J82, SW480, …) | all doses, flat |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.879× | -3.4 | 0.029 | 8/48 (SNU-1, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.3) |
| [[A-427 (line)]] | wt | 41.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -13.0) |
| [[A498 (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 32.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.4) |
| [[Hs 766T (line)]] | wt | 30.3 | 0 | 2 (1 ⚠) | — | [[Bimiralisib (drug)]] 0.5 µM 0.200× (z -8.8) |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.104× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 24.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -11.5) |
| [[SW480 (line)]] | alt | 19.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) |
| [[H4 (line)]] | wt | 38.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.158× (z -10.7) |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -10.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 22.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +8.8) | — |
| [[J82 (line)]] | alt | 51.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.4) |
| [[RKO (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.8) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -11.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.7) |
| [[A-172 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1AD]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[MAPK7]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | same gene group |
| [[CPTP]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ARL16]] | +0.65 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TINF2]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.64 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[HTRA2]] | +0.64 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[PLSCR3]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SLC52A2]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SLC35C1]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[WDR55]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TMEM115]] | +0.60 | +0.47 / +0.72 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | -0.57 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[CYB5D2]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KPNA5]] | -0.51 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[NUCKS1]] | -0.51 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[RHOBTB3]] | -0.51 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ETFRF1]] | -0.50 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[CHIC1]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RIC8A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-29.9, -12.0); signed map (-25.7, 3.4). **Vector** length 83.5, 16.1% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +8.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.8 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.0 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -3.8 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -10.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | RIC8 guanine nucleotide exchange factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:207,708-215,113 (+) |
| Ensembl biotype | protein_coding |
| Also known as | synembryn, synembryn-A |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPQ8](https://www.uniprot.org/uniprotkb/Q9NPQ8) (Chaperone Ric-8A):

> Chaperone that specifically binds and folds nascent G alpha proteins prior to G protein heterotrimer formation, promoting their stability and activity: folds GNAI1, GNAO1, GNA13 and GNAQ (By similarity). Does not fold G(s) G-alpha proteins GNAS nor GNAL (By similarity). Also acts as a guanine nucleotide exchange factor (GEF) for G alpha proteins by stimulating exchange of bound GDP for free GTP (By similarity). Involved in regulation of microtubule pulling forces during mitotic movement of …

**Summary**, from NCBI Gene [60626](https://www.ncbi.nlm.nih.gov/gene/60626):

> Predicted to enable G-protein alpha-subunit binding activity; GTPase regulator activity; and protein folding chaperone. Predicted to be involved in G protein-coupled receptor signaling pathway. Predicted to act upstream of or within several processes, including basement membrane organization; gastrulation; and visual learning. Predicted to be located in cell cortex and membrane. Predicted to be active in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29550) · Entrez [60626](https://www.ncbi.nlm.nih.gov/gene/60626) · UniProt [Q9NPQ8](https://www.uniprot.org/uniprotkb/Q9NPQ8) · Ensembl [ENSG00000177963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177963)

## Data

Gene col 10882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10882); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10882]; `tensor/DDL_lfc|DDL_z.npy` [10882]; `embed/gene_vectors.npy` [10882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10882 or target_col == 10882). Every well: [[RIC8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIC8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
