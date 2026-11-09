---
symbol: "RNF31"
type: "gene"
col: 1689
ensembl_id: "ENSG00000092098"
name: "ring finger protein 31"
location: "14q12"
module: 142
arm: "+"
pooled_cpm: 16.52
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# RNF31

*ring finger protein 31* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.30× (z +13.3, q 1e-37, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.641× (z -7.1, q 9e-10, down in 25 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.741× (z -4.8, q 3e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D10B]] (+0.60, fdr 1e-05), [[RNF4]] (+0.57, fdr 2e-05), [[MAP3K11]] (+0.57, fdr 1e-05); moves opposite to [[RFK]] (-0.50, fdr 5e-05), [[JMJD1C]] (-0.48, fdr 4e-05), [[JUN]] (-0.48, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +13.3 | 1e-37 | 42/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.2 | 2e-37 | 41/47 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +12.7 | 2e-34 | 44/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +10.7 | 1e-24 | 42/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.47×** | +10.4 | 4e-23 | 36/45 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +8.7 | 4e-16 | 35/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.2 | 6e-11 | 26/46 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.3 | 2e-08 | 25/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.0 | 1e-07 | 26/48 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 6e-04 | 16/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +3.3 | 0.052 | 10/48 (SW1417, PANC-1, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.053 | 5/47 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.053 | 13/47 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.053 | 5/47 (NCI-H2347, HCT15, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.1 | 9e-10 | 25/40 (Panc 03.27, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.677×** | -5.7 | 3e-06 | 21/36 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.700×** | -5.7 | 3e-06 | 24/46 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -4.8 | 3e-04 | 23/47 (NCI-H2347, Panc 03.27, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -4.7 | 3e-04 | 17/30 (LOX-IMVI, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.781×** | -3.6 | 0.027 | 12/46 (SW48, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.798×** | -3.6 | 0.028 | 10/48 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.862× | -3.3 | 0.064 | 15/48 (LoVo, NCI-H1792, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.821× | -3.1 | 0.11 | 15/48 (SW 900, NCI-H1573, …) | all doses, flat | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.15 | 13/48 (COLO 205, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +11.8) | — |
| [[A-172 (line)]] | wt | 12.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Valdecoxib (drug)]] 0.5 µM 0.232× (z -8.7) |
| [[LoVo (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.3) | — |
| [[A549 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -11.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.91× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 28.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D10B]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RNF4]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 | same gene group |
| [[MAP3K11]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PHF12]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[DEXI]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SERTAD3]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[DHPS]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[STAT2]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 545 |
| [[RNF121]] | +0.51 | +0.49 / +0.40 | both halves | 5e-05 | same gene group |
| [[PARGP1]] | +0.51 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[MVP]] | +0.50 | +0.53 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[SAP130]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[JMJD1C]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[JUN]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[LINC00705]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CREB5]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GCFC2]] | -0.46 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD20A5P]] | -0.44 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNF31's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, -28.8); signed map (-40.4, 4.7). **Vector** length 86.5, 17.4% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.9 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +0.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.9 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,146,683-24,160,660 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZIBRA, FLJ10111, FLJ23501, HOIP, Paul |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers RANBP2-type; Linear ubiquitin chain assembly complex; RBR E3 ubiquitin ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Regulation of TNFR1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EP0](https://www.uniprot.org/uniprotkb/Q96EP0) (E3 ubiquitin-protein ligase RNF31):

> E3 ubiquitin-protein ligase component of the LUBAC complex which conjugates linear ('Met-1'-linked) polyubiquitin chains to substrates and plays a key role in NF-kappa-B activation and regulation of inflammation. RNF31 constitutes the catalytic subunit of the LUBAC complex and specifically mediates the synthesis of linear ubiquitin chains. LUBAC conjugates linear polyubiquitin to IKBKG and RIPK1 and is involved in activation of the canonical NF-kappa-B and the JNK signaling pathways. Linear …

**Summary**, from NCBI Gene [55072](https://www.ncbi.nlm.nih.gov/gene/55072):

> The protein encoded by this gene contains a RING finger, a motif present in a variety of functionally distinct proteins and known to be involved in protein-DNA and protein-protein interactions. The encoded protein is the E3 ubiquitin-protein ligase component of the linear ubiquitin chain assembly complex. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:16031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16031) · Entrez [55072](https://www.ncbi.nlm.nih.gov/gene/55072) · UniProt [Q96EP0](https://www.uniprot.org/uniprotkb/Q96EP0) · Ensembl [ENSG00000092098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092098)

## Data

Gene col 1689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1689); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1689]; `tensor/DDL_lfc|DDL_z.npy` [1689]; `embed/gene_vectors.npy` [1689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1689 or target_col == 1689). Every well: [[RNF31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
