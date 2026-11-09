---
symbol: "MIS12"
type: "gene"
col: 9549
ensembl_id: "ENSG00000167842"
name: "MIS12 kinetochore complex component"
location: "17p13.2"
module: 16
arm: "+"
pooled_cpm: 12.37
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# MIS12

*MIS12 kinetochore complex component* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +23.0, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.798× (z -5.4, q 3e-05, down in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.147×; ⚠ cell-cycle shift, explains ~62% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.0904×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.193×; ⚠ cell-cycle shift, explains ~27% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0804×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SP2]] (+0.73, fdr 7e-06), [[MAGOHB]] (+0.72, fdr 7e-06), [[ZNF268]] (+0.72, fdr 7e-06); moves opposite to [[RPS24]] (-0.71, fdr 7e-06), [[HDAC3]] (-0.70, fdr 7e-06), [[RPS25]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.62×** | +23.0 | 0e+00 | 43/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.90×** | +17.3 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.64×** | +16.4 | 0e+00 | 42/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.07×** | +12.3 | 1e-32 | 23/33 (SW480, NCI-H1573, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +12.2 | 3e-32 | 37/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.07×** | +11.8 | 3e-30 | 16/23 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.03×** | +11.1 | 2e-26 | 24/28 (NCI-H460, NCI-H2030, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +7.9 | 1e-13 | 25/47 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +7.5 | 5e-12 | 21/43 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.2 | 2e-11 | 23/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +7.2 | 2e-11 | 23/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.2 | 3e-11 | 22/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.49×** | +6.4 | 5e-09 | 14/37 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.42×** | +5.9 | 1e-07 | 18/47 (A549, SW480, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.0 | 3e-05 | 16/47 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.007 | 2/47 (SW1417, J82) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +3.5 | 0.012 | 5/48 (J82, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.032 | 13/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.048 | 6/44 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.083 | 3/46 (SW480, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +2.8 | 0.084 | 7/47 (A498, SW 1271, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9549.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.147×; ⚠ cell-cycle shift, explains ~62% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.0904×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.193×; ⚠ cell-cycle shift, explains ~27% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0804×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.798×** | -5.4 | 3e-05 | 10/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.056 | 12/47 (NCI-H2030, A498, …) | rises with dose | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | 0.832× | -3.1 | 0.25 | 8/47 (AsPC-1, SW 1271, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.835× | -3.1 | 0.25 | 9/46 (SNU-423, RKO, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | 0.708× | -3.1 | 0.25 | 11/44 (A498, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.2 | 7 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.42× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 14.8 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.65× (z +10.2) | — |
| [[A549 (line)]] | wt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 8.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.4) | — |
| [[J82 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.5) | — |
| [[A-172 (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0904× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 8.92 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0804× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.18× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 9.32 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.14× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.1) | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP2]] | +0.73 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[MAGOHB]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.72 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[TASOR]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[MLH1]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.70 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.68 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.68 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[FBXO38]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.68 | +0.71 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS24]] | -0.71 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[HDAC3]] | -0.70 | -0.71 / -0.58 | both halves | 7e-06 |  |
| [[RPS25]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[NME2]] | -0.69 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[NENF]] | -0.68 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[SEC11A]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.68 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[SCAI]] | -0.67 | -0.64 / -0.61 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[NFRKB]] | -0.67 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[RNF149]] | -0.67 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[RPL12]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[NDUFAF7]] | -0.67 | -0.63 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity raises MIS12's level | compounds that target ABL1: 2 of 6 lower it (Ponatinib, Radotinib) | 33% of the class's compounds vs 0.6% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds |
| [[DUXAP10]] | B | DUXAP10 activity raises MIS12's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.16× lower at baseline in the lines without DUXAP10 | 0.095 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.0, 1.9); signed map (15.7, -27.5). **Vector** length 81.4, 15.2% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +16.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +23.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.2 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +3.0 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MIS12 kinetochore complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,486,285-5,490,814 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2488, hMIS12, KNTC2AP, MTW1 |
| Gene groups (HGNC) | MIS12 kinetochore complex |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H081](https://www.uniprot.org/uniprotkb/Q9H081) (Protein MIS12 homolog):

> Part of the MIS12 complex which is required for normal chromosome alignment and segregation and for kinetochore formation during mitosis. Essential for proper kinetochore microtubule attachments.

**Summary**, from NCBI Gene [79003](https://www.ncbi.nlm.nih.gov/gene/79003):

> Involved in attachment of mitotic spindle microtubules to kinetochore and kinetochore assembly. Located in kinetochore and nucleus. Part of MIS12/MIND type complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24967) · Entrez [79003](https://www.ncbi.nlm.nih.gov/gene/79003) · UniProt [Q9H081](https://www.uniprot.org/uniprotkb/Q9H081) · Ensembl [ENSG00000167842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167842)

## Data

Gene col 9549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9549); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9549]; `tensor/DDL_lfc|DDL_z.npy` [9549]; `embed/gene_vectors.npy` [9549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9549 or target_col == 9549). Every well: [[MIS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
