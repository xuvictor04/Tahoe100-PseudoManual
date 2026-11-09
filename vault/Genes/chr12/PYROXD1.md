---
symbol: "PYROXD1"
type: "gene"
col: 4268
ensembl_id: "ENSG00000121350"
name: "pyridine nucleotide-disulphide oxidoreductase domain 1"
location: "12p12.1"
module: 63
arm: "+"
pooled_cpm: 40.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PYROXD1

*pyridine nucleotide-disulphide oxidoreductase domain 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.40× (z +7.6, q 2e-11, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.562× (z -9.2, q 2e-17, down in 28 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -8.1, q 9e-14, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARL]] (+0.67, fdr 7e-06), [[LINC01012]] (+0.67, fdr 1e-05), [[FRG1BP]] (+0.66, fdr 1e-05); moves opposite to [[PRKCA]] (-0.50, fdr 4e-05), [[CFL1]] (-0.50, fdr 4e-05), [[SRGAP2]] (-0.49, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +7.6 | 2e-11 | 40/49 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +6.7 | 6e-09 | 35/47 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.84×** | +5.2 | 3e-05 | 29/46 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.7 | 3e-04 | 23/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +4.5 | 9e-04 | 24/48 (SNU-1, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.002 | 21/48 (SNU-1, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.8 | 0.010 | 16/48 (HT-29, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.010 | 17/48 (NCI-H2030, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.7 | 0.012 | 18/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.012 | 19/47 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.022 | 14/47 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.026 | 19/47 (LOX-IMVI, Panc 03.27, …) | rises with dose | composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.026 | 18/47 (SNU-1, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.23×** | +3.4 | 0.027 | 16/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.027 | 17/48 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.033 | 18/47 (SNU-1, HCT15, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.078 | 15/48 (Hs 766T, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4268.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.562×** | -9.2 | 2e-17 | 28/37 (KATO III, SNU-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.609×** | -8.2 | 6e-14 | 36/48 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -8.1 | 9e-14 | 36/47 (LOX-IMVI, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.621×** | -7.9 | 4e-13 | 39/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.663×** | -6.8 | 1e-09 | 30/48 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.695×** | -6.0 | 2e-07 | 29/48 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.698×** | -5.7 | 8e-07 | 33/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.731×** | -5.2 | 1e-05 | 26/46 (SK-MEL-2, HCT15, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.729×** | -5.1 | 3e-05 | 24/47 (H4, C32, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.004 | 20/48 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.787×** | -4.0 | 0.004 | 22/47 (LoVo, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.819×** | -3.3 | 0.041 | 22/45 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.684×** | -3.3 | 0.043 | 10/48 (A498, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.827×** | -3.2 | 0.064 | 13/47 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.2) |
| [[SNU-1 (line)]] | wt | 81.4 | 0 | 3 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0719× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -9.1) |
| [[H4 (line)]] | wt | 45.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.39× (z +8.7) ⚠ toxic | — |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 74.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.95× (z +13.6) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 61.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[SW1417 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-172 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARL]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[LINC01012]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[FRG1BP]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TCEA1]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.61 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[DUSP12]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZFAND1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MTO1]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 | same gene group |
| [[PIGB]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RSL24D1]] | +0.59 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[RTCA]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKCA]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CFL1]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[SRGAP2]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PYROXD1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.8, 1.7); signed map (-24.8, -10.7). **Vector** length 90.1, 20.5% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.50 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +1.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.2 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.7 | +3.2 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | +0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | pyridine nucleotide-disulphide oxidoreductase domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,437,615-21,471,250 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762G094, FLJ22028 |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WU10](https://www.uniprot.org/uniprotkb/Q8WU10) (tRNA ligase complex-associated NAD(P)H dehydrogenase PYROXD1):

> Flavoprotein whose role is to protect RTCB, the catalytic subunit of the tRNA ligase complex (tRNA-LC) involved in tRNA splicing and unfolded protein response, from oxidative inactivation. It directly binds and shields the catalytic center of RTCB, prior to guanylylation, when it is inactive and its active site is vulnerable to oxidation under aerobic conditions. The interaction of PYROXD1 with RTCB is allosterically regulated by NAD(P)H binding and reduction of its FAD cofactor, while …

**Summary**, from NCBI Gene [79912](https://www.ncbi.nlm.nih.gov/gene/79912):

> This gene encodes a nuclear-cytoplasmic pyridine nucleotide-disulphide reductase (PNDR). PNDRs are flavoproteins that catalyze the pyridine nucleotide-dependent reduction of thiol residues in other proteins. The encoded protein belongs to the class I pyridine nucleotide-disulphide oxidoreductase family but lacks the C-terminal dimerization domain found in other family members and instead has a C-terminal nitrile reductase domain. It localizes to the nucleus and to striated sarcomeric …

**Accessions** — [HGNC:26162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26162) · Entrez [79912](https://www.ncbi.nlm.nih.gov/gene/79912) · UniProt [Q8WU10](https://www.uniprot.org/uniprotkb/Q8WU10) · Ensembl [ENSG00000121350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121350)

## Data

Gene col 4268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4268); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4268]; `tensor/DDL_lfc|DDL_z.npy` [4268]; `embed/gene_vectors.npy` [4268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4268 or target_col == 4268). Every well: [[PYROXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYROXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
