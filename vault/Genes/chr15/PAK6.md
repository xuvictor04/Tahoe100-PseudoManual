---
symbol: "PAK6"
type: "gene"
col: 6084
ensembl_id: "ENSG00000137843"
name: "p21 (RAC1) activated kinase 6"
location: "15q15.1"
module: 22
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PAK6

*p21 (RAC1) activated kinase 6* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +6.6, q 2e-08, up in 11 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.35× (z +4.3, q 0.003, up in 7 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.597× (z -7.4, q 9e-11, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1B]] (+0.86, fdr 7e-06, ⚠ same locus), [[TACC3]] (+0.86, fdr 7e-06), [[GTSE1]] (+0.85, fdr 7e-06), [[KIF4A]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6084.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.59×** | +6.6 | 2e-08 | 11/33 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.42×** | +5.0 | 2e-04 | 11/36 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.38×** | +4.5 | 0.001 | 8/16 (HT-29, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.003 | 7/45 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[AZD1390 (drug)]] 0.05 µM |  | 1.27× | +3.3 | 0.11 | 7/45 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.16× | +3.1 | 0.13 | 5/46 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | 1.26× | +3.1 | 0.13 | 6/22 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.24× | +3.1 | 0.13 | 11/44 (A549, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.13 | 6/43 (BT-474, RKO, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.13 | 3/42 (A549, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6084.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -7.4 | 9e-11 | 25/44 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.652×** | -6.1 | 3e-07 | 20/43 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.743×** | -6.0 | 4e-07 | 19/45 (LOX-IMVI, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.668×** | -5.8 | 1e-06 | 21/44 (H4, C32, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -5.7 | 2e-06 | 17/45 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.748×** | -4.1 | 0.003 | 12/45 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.747×** | -3.9 | 0.007 | 15/42 (AN3 CA, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.774×** | -3.6 | 0.019 | 8/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.779×** | -3.4 | 0.038 | 8/43 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.795×** | -3.3 | 0.060 | 8/45 (SW1417, NCI-H460, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.727×** | -3.2 | 0.060 | 5/46 (SNU-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.856× | -3.1 | 0.075 | 13/45 (A549, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.804×** | -3.1 | 0.075 | 14/43 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.075 | 8/44 (RKO, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.085 | 8/42 (LoVo, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6084. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.101× (z -10.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[LOX-IMVI (line)]] | wt | 6.44 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -10.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.136× (z -10.7) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.86 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.126× (z -9.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[Hs 766T (line)]] | wt | 4.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0748× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 8.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.54 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0858× (z -9.3) |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0516× (z -9.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6084), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1B]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TACC3]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.84 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[KIF23]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[KIF14]] | +0.84 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 |  |
| [[MKI67]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[ARHGAP11B]] | +0.82 | +0.75 / +0.81 | both halves | 7e-06 | pathway: CDC42 GTPase cycle |
| [[TROAP]] | +0.82 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[PRC1]] | +0.82 | +0.80 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises PAK6's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without PIMREG | 0.037 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises PAK6's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without NDC80 | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises PAK6's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without PBK | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.841). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.6, -55.6); signed map (-49.2, -42.4). **Vector** length 86.3, 17.4% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.67 to 60); *DREAM G2/M down* (control, mean cos +0.76 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.63 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.9 | +4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.6 | +3.1 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +2.5 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | +2.5 | +5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.7 | +2.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.4 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -2.4 | -6.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | p21 (RAC1) activated kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,217,428-40,277,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAK5 |
| Gene groups (HGNC) | p21 (RAC1) activated kinase family |
| Reactome | 12 pathways, smallest: Activation of RAC1; RHOH GTPase cycle; RHOV GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQU5](https://www.uniprot.org/uniprotkb/Q9NQU5) (Serine/threonine-protein kinase PAK 6):

> Serine/threonine protein kinase that plays a role in the regulation of gene transcription. The kinase activity is induced by various effectors including AR or MAP2K6/MAPKK6. Phosphorylates the DNA-binding domain of androgen receptor/AR and thereby inhibits AR-mediated transcription. Also inhibits ESR1-mediated transcription. May play a role in cytoskeleton regulation by interacting with IQGAP1. May protect cells from apoptosis through phosphorylation of BAD.

**Summary**, from NCBI Gene [56924](https://www.ncbi.nlm.nih.gov/gene/56924):

> This gene encodes a member of a family of p21-stimulated serine/threonine protein kinases, which contain an amino-terminal Cdc42/Rac interactive binding (CRIB) domain and a carboxyl-terminal kinase domain. These kinases function in a number of cellular processes, including cytoskeleton rearrangement, apoptosis, and the mitogen-activated protein (MAP) kinase signaling pathway. The protein encoded by this gene interacts with androgen receptor (AR) and translocates to the nucleus, where it is …

**Accessions** — [HGNC:16061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16061) · Entrez [56924](https://www.ncbi.nlm.nih.gov/gene/56924) · UniProt [Q9NQU5](https://www.uniprot.org/uniprotkb/Q9NQU5) · Ensembl [ENSG00000137843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137843)

## Data

Gene col 6084: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6084); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6084, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6084]; `tensor/DDL_lfc|DDL_z.npy` [6084]; `embed/gene_vectors.npy` [6084]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6084 or target_col == 6084). Every well: [[PAK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
