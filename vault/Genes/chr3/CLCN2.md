---
symbol: "CLCN2"
type: "gene"
col: 3597
ensembl_id: "ENSG00000114859"
name: "chloride voltage-gated channel 2"
location: "3q27.1"
module: 23
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CLCN2

*chloride voltage-gated channel 2* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +19.0, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.705× (z -5.5, q 2e-05, down in 20 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.735× (z -4.8, q 4e-04, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF3]] (+0.56, fdr 3e-05), [[MAP3K11]] (+0.52, fdr 3e-05), [[TRPM4]] (+0.50, fdr 4e-05); moves opposite to [[GTDC1]] (-0.46, fdr 1e-04), [[PALLD]] (-0.44, fdr 5e-04), [[MAP2]] (-0.43, fdr 6e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +19.0 | 0e+00 | 40/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +13.2 | 4e-37 | 37/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.89×** | +10.0 | 3e-21 | 36/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.86×** | +9.7 | 4e-20 | 32/44 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.64×** | +7.8 | 6e-13 | 27/47 (PANC-1, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.8 | 7e-10 | 24/43 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.7 | 2e-09 | 23/44 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.5 | 4e-09 | 21/43 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 1e-04 | 17/43 (LoVo, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 15/46 (SW1417, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.9 | 0.005 | 11/48 (BT-474, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.30×** | +3.9 | 0.005 | 12/37 (NCI-H460, NCI-H1792, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.25×** | +3.5 | 0.017 | 12/47 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.1 | 0.088 | 9/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.093 | 3/47 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -5.5 | 2e-05 | 20/45 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.735×** | -4.8 | 4e-04 | 14/46 (COLO 205, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -4.5 | 0.001 | 16/37 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 0.002 | 16/47 (SK-MEL-2, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.004 | 17/47 (hTERT-HPNE, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.022 | 13/46 (NCI-H2347, NCI-H2030, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.793×** | -3.6 | 0.022 | 11/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.800×** | -3.5 | 0.033 | 13/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Decitabine (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.083 | 10/43 (SW48, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.807× | -3.1 | 0.10 | 5/16 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.12 | 13/44 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.12 | 6/44 (SNU-423, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.4 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.0656× (z -19.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 23.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.12 | 0 | 2 | — | [[Vilanterol (drug)]] 0.5 µM 0.0699× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 3.77 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +10.2) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.132× (z -8.6) |
| [[HCT15 (line)]] | alt | 9.85 | 0 | 1 | — | [[Mebendazole (drug)]] 0.05 µM 0.0594× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 8.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +8.7) | — |
| [[SW480 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF3]] | +0.56 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[MAP3K11]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TRPM4]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 | pathway: Ion channel transport |
| [[RALY-AS1]] | +0.49 | +0.39 / +0.39 | both halves | 5e-05 |  |
| [[ZNF101]] | +0.48 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[HOXB4]] | +0.48 | +0.25 / +0.44 | both halves | 4e-04 |  |
| [[MYADM-AS1]] | +0.48 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[PROCA1]] | +0.47 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[RNF31]] | +0.47 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[RECQL5]] | +0.47 | +0.32 / +0.39 | both halves | 2e-04 |  |
| [[PLCG1]] | +0.46 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[TGFB3]] | +0.46 | +0.48 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTDC1]] | -0.46 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[PALLD]] | -0.44 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[MAP2]] | -0.43 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[GDE1]] | -0.42 | -0.17 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[EFR3A]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[TXNRD1]] | -0.40 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[PIR]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[NBEA]] | -0.40 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[LRRC28]] | -0.39 | -0.26 / -0.29 | both halves | 4e-04 |  |
| [[CAPN7]] | -0.39 | -0.30 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLCN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.137). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (23.4, -28.8); signed map (4.7, 9.7). **Vector** length 75.9, 12.8% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +19.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +9.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.4 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +0.2 |
|  | [[Posaconazole (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | chloride voltage-gated channel 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,346,185-184,361,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLC2, EJM6, ClC-2 |
| Gene groups (HGNC) | CLC chloride channel and transporter family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P51788](https://www.uniprot.org/uniprotkb/P51788) (Chloride channel protein 2):

> Voltage-gated and osmosensitive chloride channel. Forms a homodimeric channel where each subunit has its own ion conduction pathway. Conducts double-barreled currents controlled by two types of gates, two fast glutamate gates that control each subunit independently and a slow common gate that opens and shuts off both subunits simultaneously. Displays inward rectification currents activated upon membrane hyperpolarization and extracellular hypotonicity. Contributes to chloride conductance …

**Summary**, from NCBI Gene [1181](https://www.ncbi.nlm.nih.gov/gene/1181):

> This gene encodes a voltage-gated chloride channel. The encoded protein is a transmembrane protein that maintains chloride ion homeostasis in various cells. Defects in this gene may be a cause of certain epilepsies. Four transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:2020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2020) · Entrez [1181](https://www.ncbi.nlm.nih.gov/gene/1181) · UniProt [P51788](https://www.uniprot.org/uniprotkb/P51788) · Ensembl [ENSG00000114859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114859)

## Data

Gene col 3597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3597); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3597]; `tensor/DDL_lfc|DDL_z.npy` [3597]; `embed/gene_vectors.npy` [3597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3597 or target_col == 3597). Every well: [[CLCN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLCN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
