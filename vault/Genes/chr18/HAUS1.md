---
symbol: "HAUS1"
type: "gene"
col: 7607
ensembl_id: "ENSG00000152240"
name: "HAUS augmin like complex subunit 1"
location: "18q21.1"
module: 6
arm: "+"
pooled_cpm: 15.31
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HAUS1

*HAUS augmin like complex subunit 1* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +11.8, q 4e-29, up in 21 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.52×, MIA PaCa-2 4.40×, SW480 2.98×, PANC-1 3.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.59×, Hs 766T 5.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -12.6, q 7e-34, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRIM1]] (+0.84, fdr 7e-06), [[DSCC1]] (+0.79, fdr 7e-06), [[MMS22L]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRCC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7607.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.52×, MIA PaCa-2 4.40×, SW480 2.98×, PANC-1 3.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.59×, Hs 766T 5.63×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.55×** | +11.8 | 4e-29 | 21/27 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.32×** | +11.0 | 1e-25 | 34/40 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.63×** | +5.9 | 7e-07 | 22/33 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +4.7 | 4e-04 | 23/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.39×** | +4.3 | 0.002 | 20/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.37×** | +4.1 | 0.004 | 17/41 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.27× | +3.1 | 0.13 | 10/47 (MIA PaCa-2, HEC-1-A, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.504×** | -12.6 | 7e-34 | 40/47 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -7.5 | 1e-11 | 37/47 (SNU-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -7.5 | 1e-11 | 30/46 (A-427, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -6.0 | 3e-07 | 27/46 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -4.6 | 5e-04 | 22/47 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -4.4 | 1e-03 | 22/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.536×** | -4.3 | 0.002 | 23/45 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.639× | -3.1 | 0.13 | 6/48 (HEC-1-A, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.780× | -3.1 | 0.14 | 14/48 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.0 | 0.15 | 4/48 (J82, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.0) |
| [[A-427 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -12.2) |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0823× (z -8.9) |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.138× (z -9.3) |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 9.11 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0795× (z -9.5) |
| [[Hs 766T (line)]] | wt | 14.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.6) |
| [[KATO III (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.7) |
| [[PANC-1 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM1]] | +0.84 | +0.77 / +0.81 | both halves | 7e-06 | STRING 418 |
| [[DSCC1]] | +0.79 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.79 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[CEP78]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 | pathway: AURKA Activation by TPX2; STRING 535 |
| [[MSH2]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[RFC5]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[RRM1]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[RFC4]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 | STRING 784 |
| [[CENPU]] | +0.74 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[ORC1]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[RBL1]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[POLD3]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRCC1]] | C | LRRCC1 activity lowers HAUS1's level | lines that do not express LRRCC1 (4) vs lines expressing it (46) | 2.07× higher at baseline in the lines without LRRCC1 | 0.040 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.1, -44.6); signed map (-36.1, -42.3). **Vector** length 67.9, 12.6% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 65); *DNA strand elongation* (reactome, mean cos +0.59 to 28); *DNA Replication* (reactome, mean cos +0.59 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.0 | +11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.8 | -3.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:46,104,378-46,128,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEI-C, HsT1461, FLJ40084; previously CCDC5 |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CS2](https://www.uniprot.org/uniprotkb/Q96CS2) (HAUS augmin-like complex subunit 1):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [115106](https://www.ncbi.nlm.nih.gov/gene/115106):

> HAUS1 is 1 of 8 subunits of the 390-kD human augmin complex, or HAUS complex. The augmin complex was first identified in Drosophila, and its name comes from the Latin verb 'augmentare,' meaning 'to increase.' The augmin complex is a microtubule-binding complex involved in microtubule generation within the mitotic spindle and is vital to mitotic spindle assembly (Goshima et al., 2008 [PubMed 18443220]; Uehara et al., 2009 [PubMed 19369198]).[supplied by OMIM, Jun 2010]

**Accessions** — [HGNC:25174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25174) · Entrez [115106](https://www.ncbi.nlm.nih.gov/gene/115106) · UniProt [Q96CS2](https://www.uniprot.org/uniprotkb/Q96CS2) · Ensembl [ENSG00000152240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152240)

## Data

Gene col 7607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7607); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7607]; `tensor/DDL_lfc|DDL_z.npy` [7607]; `embed/gene_vectors.npy` [7607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7607 or target_col == 7607). Every well: [[HAUS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
