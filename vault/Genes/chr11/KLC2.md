---
symbol: "KLC2"
type: "gene"
col: 10550
ensembl_id: "ENSG00000174996"
name: "kinesin light chain 2"
location: "11q13.2"
module: 126
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# KLC2

*kinesin light chain 2* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.51× (z +10.5, q 8e-23, up in 20 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.85× (z +7.3, q 5e-11, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.789× (z -4.1, q 0.029, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0666×); [[Simotinib (drug)]] 0.05 µM in 1 line (C32 0.0980×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.119×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBN1]] (+0.79, fdr 7e-06), [[UBQLN4]] (+0.73, fdr 7e-06), [[CERS2]] (+0.70, fdr 7e-06); moves opposite to [[TRIM7-AS2]] (-0.64, fdr 1e-05), [[PITPNA-AS1]] (-0.62, fdr 2e-05), [[MINCR]] (-0.59, fdr 4e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +10.5 | 8e-23 | 20/23 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +9.9 | 1e-20 | 28/36 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.9 | 4e-13 | 25/29 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +7.3 | 5e-11 | 33/46 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.5 | 7e-09 | 26/46 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.2 | 6e-08 | 24/45 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +5.7 | 8e-07 | 27/46 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.7 | 8e-07 | 25/41 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +5.7 | 8e-07 | 24/46 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +5.4 | 4e-06 | 24/46 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.61×** | +5.4 | 4e-06 | 21/39 (NCI-H2030, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +5.3 | 5e-06 | 20/45 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +5.3 | 6e-06 | 25/46 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 16/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 4e-04 | 18/46 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 9e-04 | 18/47 (NCI-H2347, SNU-423, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 16/46 (A498, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.005 | 18/45 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.006 | 7/46 (SW480, HEC-1-A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.013 | 15/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.030 | 9/43 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.073 | 15/46 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10550.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0666×); [[Simotinib (drug)]] 0.05 µM in 1 line (C32 0.0980×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM |  | **0.789×** | -4.1 | 0.029 | 17/47 (SW 1088, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 10.6 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0980× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0666× (z -10.5) |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.119× (z -8.6) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBN1]] | +0.79 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[UBQLN4]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[CERS2]] | +0.70 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PSME3]] | +0.67 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[ELK4]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.66 | +0.55 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANKRD52]] | +0.63 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.63 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[MAPRE1]] | +0.62 | +0.43 / +0.64 | both halves | 3e-05 | pathway: RHO GTPase Effectors |
| [[MTA2]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[PITPNA-AS1]] | -0.62 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[MINCR]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[LAMTOR5]] | -0.58 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[CTR9]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 | same gene group; pathway: Affinity selection of immunoglobulins |
| [[ATP5MC2]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[MALSU1]] | -0.56 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[NDUFA7]] | -0.56 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[SUMO4]] | -0.56 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[SIRT2]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | -0.56 | -0.40 / -0.56 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX14]] | -0.55 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[TOGARAM1]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.9, -23.7); signed map (-12.9, -36.3). **Vector** length 84.1, 16.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.9 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | kinesin light chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,257,294-66,267,860 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12387 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Reactome | 17 pathways, smallest: RHO GTPases activate KTN1; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0B6](https://www.uniprot.org/uniprotkb/Q9H0B6) (Kinesin light chain 2):

> Kinesin is a microtubule-associated force-producing protein that plays a role in organelle transport. The light chain functions in coupling of cargo to the heavy chain or in the modulation of its ATPase activity (Probable). Through binding with PLEKHM2 and ARL8B, recruits kinesin-1 to lysosomes and hence direct lysosomes movement toward microtubule plus ends.

**Summary**, from NCBI Gene [64837](https://www.ncbi.nlm.nih.gov/gene/64837):

> The protein encoded by this gene is a light chain of kinesin, a molecular motor responsible for moving vesicles and organelles along microtubules. Defects in this gene are a cause of spastic paraplegia, optic atrophy, and neuropathy (SPOAN) syndrome. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:20716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20716) · Entrez [64837](https://www.ncbi.nlm.nih.gov/gene/64837) · UniProt [Q9H0B6](https://www.uniprot.org/uniprotkb/Q9H0B6) · Ensembl [ENSG00000174996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174996)

## Data

Gene col 10550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10550); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10550]; `tensor/DDL_lfc|DDL_z.npy` [10550]; `embed/gene_vectors.npy` [10550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10550 or target_col == 10550). Every well: [[KLC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
