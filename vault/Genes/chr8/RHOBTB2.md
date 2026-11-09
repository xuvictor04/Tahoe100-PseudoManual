---
symbol: "RHOBTB2"
type: "gene"
col: 181
ensembl_id: "ENSG00000008853"
name: "Rho related BTB domain containing 2"
location: "8p21.3"
module: 97
arm: "+"
pooled_cpm: 5.73
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# RHOBTB2

*Rho related BTB domain containing 2* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.49× (z +13.9, q 7e-41, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.681× (z -4.3, q 0.010, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFBR2]] (+0.63, fdr 7e-06), [[CCND3]] (+0.62, fdr 1e-05), [[MAOA]] (+0.61, fdr 1e-05); moves opposite to [[RBCK1]] (-0.54, fdr 1e-05), [[PMS2P4-1]] (-0.54, fdr 4e-05), [[METTL21A]] (-0.53, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTPRU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.49×** | +13.9 | 7e-41 | 42/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.25×** | +13.1 | 2e-36 | 42/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.22×** | +13.0 | 3e-36 | 42/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.66×** | +10.4 | 2e-23 | 7/8 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.30×** | +9.2 | 3e-18 | 22/32 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +8.1 | 3e-14 | 29/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.21×** | +8.1 | 4e-14 | 14/16 (A-172, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.1 | 9e-11 | 28/46 (SW480, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +5.2 | 1e-05 | 15/40 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.0 | 3e-05 | 10/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 2e-04 | 14/44 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +4.4 | 4e-04 | 5/45 (A-172, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.47×** | +4.3 | 7e-04 | 5/45 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +4.3 | 7e-04 | 14/45 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 7e-04 | 17/39 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 13/45 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.002 | 11/44 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.005 | 11/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.005 | 10/45 (NCI-H460, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.013 | 12/44 (NCI-H460, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -4.3 | 0.010 | 20/46 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.781×** | -3.9 | 0.027 | 15/46 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.715×** | -3.7 | 0.034 | 16/45 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.042 | 15/45 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.062 | 14/45 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.071 | 5/47 (NCI-H2347, SHP-77, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.742×** | -3.3 | 0.071 | 12/45 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.757× | -3.1 | 0.13 | 11/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 7.52 | 0 | 2 | — | [[Penfluridol (drug)]] 5 µM 0.0750× (z -10.0) |
| [[A-172 (line)]] | wt | 9.91 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.51× (z +9.1) | — |
| [[A498 (line)]] | wt | 5.99 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.98× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0816× (z -8.5) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0723× (z -9.7) |
| [[SW480 (line)]] | alt | 6.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBR2]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCND3]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MAOA]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ADRA1B]] | +0.58 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[SHROOM2]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[THEM6]] | +0.57 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[EMP2]] | +0.56 | +0.28 / +0.61 | both halves | 3e-04 |  |
| [[ZHX3]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[TRNP1]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PHACTR3]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TANC2]] | +0.54 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[TIPARP]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBCK1]] | -0.54 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[METTL21A]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[NRSN2-AS1]] | -0.53 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[CBR3-AS1]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[PLPP5]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SPAG7]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[TMEM106A]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TSNAX-DISC1]] | -0.50 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[MFSD8]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRU]] | B | PTPRU activity raises RHOBTB2's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without PTPRU | 0.069 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[TRNP1]] | B | TRNP1 activity lowers RHOBTB2's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without TRNP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 12.4); signed map (14.2, 33.1). **Vector** length 60.7, 8.87% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.7 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.7 | +8.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.1 | +4.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.0 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho related BTB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,987,417-23,020,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0717, DBC2 |
| Gene groups (HGNC) | Rho family GTPases; BTB domain containing |
| Reactome | 5 pathways, smallest: RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYZ6](https://www.uniprot.org/uniprotkb/Q9BYZ6) (Rho-related BTB domain-containing protein 2):

> Regulator of cell proliferation and apoptosis. It likely functions as a substrate-adapter that recruits key substrates, e.g. MSI2, to CUL3-based ubiquitin ligase complexes for degradation. Required for MSI2 ubiquitination and degradation.

**Summary**, from NCBI Gene [23221](https://www.ncbi.nlm.nih.gov/gene/23221):

> The protein encoded by this gene is a small Rho GTPase and a candidate tumor suppressor. The encoded protein interacts with the cullin-3 protein, a ubiquitin E3 ligase necessary for mitotic cell division. This protein inhibits the growth and spread of some types of breast cancer. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:18756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18756) · Entrez [23221](https://www.ncbi.nlm.nih.gov/gene/23221) · UniProt [Q9BYZ6](https://www.uniprot.org/uniprotkb/Q9BYZ6) · Ensembl [ENSG00000008853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008853)

## Data

Gene col 181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 181); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 181]; `tensor/DDL_lfc|DDL_z.npy` [181]; `embed/gene_vectors.npy` [181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 181 or target_col == 181). Every well: [[RHOBTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOBTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
