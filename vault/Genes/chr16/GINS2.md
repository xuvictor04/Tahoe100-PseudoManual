---
symbol: "GINS2"
type: "gene"
col: 5179
ensembl_id: "ENSG00000131153"
name: "GINS complex subunit 2"
location: "16q24.1"
module: 6
arm: "+"
pooled_cpm: 6.75
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GINS2

*GINS complex subunit 2* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.33× (z +13.7, q 5e-40, up in 46 of 46 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.57× (z +4.1, q 0.002, up in 14 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -8.3, q 5e-14, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.91, fdr 7e-06), [[EXO1]] (+0.90, fdr 7e-06), [[TCF19]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **4.33×** | +13.7 | 5e-40 | 46/46 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **3.77×** | +12.4 | 5e-33 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **3.66×** | +12.2 | 1e-31 | 20/24 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **3.38×** | +11.0 | 9e-26 | 11/12 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **2.97×** | +10.2 | 2e-22 | 41/46 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.85×** | +8.2 | 3e-14 | 25/39 (A549, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **2.49×** | +7.9 | 2e-13 | 11/14 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **2.14×** | +6.8 | 5e-10 | 18/30 (SW480, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.90×** | +5.8 | 4e-07 | 18/36 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.42×** | +4.7 | 2e-04 | 12/47 (SW480, HCT15, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 14/43 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.57×** | +4.1 | 0.002 | 8/43 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.51×** | +3.9 | 0.005 | 9/28 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 12/46 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.50×** | +3.7 | 0.009 | 16/41 (SW480, BT-474, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.47×** | +3.6 | 0.012 | 9/44 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.062 | 4/44 (LoVo, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -8.3 | 5e-14 | 26/40 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.447×** | -7.5 | 1e-11 | 23/37 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.604×** | -4.7 | 5e-04 | 18/42 (A-172, LS 180, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.725×** | -4.3 | 0.003 | 20/45 (KATO III, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.627×** | -4.2 | 0.003 | 13/41 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.545×** | -3.8 | 0.012 | 12/45 (SW480, AN3 CA, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.761×** | -3.6 | 0.025 | 18/45 (A498, RKO, …) | all doses, flat | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.464×** | -3.5 | 0.029 | 7/46 (H4, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.688×** | -3.4 | 0.050 | 16/42 (A-172, A-427, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.592×** | -3.3 | 0.053 | 7/47 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.690×** | -3.3 | 0.054 | 15/43 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.694×** | -3.2 | 0.059 | 11/46 (RKO, C32, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.717×** | -3.1 | 0.083 | 13/42 (Hs 766T, SW480, …) | rises with dose | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.514×** | -3.1 | 0.090 | 8/47 (LS 180, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **0.715×** | -3.0 | 0.096 | 5/46 (NCI-H661, LOX-IMVI, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.55 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.0 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.241× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -11.0) |
| [[HOP62 (line)]] | alt | 5.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.8) |
| [[RKO (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0694× (z -11.4) |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.260× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.7) |
| [[LS 180 (line)]] | wt | 6.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 8.45 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.237× (z -8.5) |
| [[SW480 (line)]] | alt | 7.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.1) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[EXO1]] | +0.90 | +0.90 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 601 |
| [[TCF19]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | STRING 616 |
| [[RAD54L]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 520 |
| [[WDR76]] | +0.87 | +0.88 / +0.86 | both halves | 7e-06 | STRING 574 |
| [[MCM10]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | pathway: DNA Replication; STRING 938 |
| [[E2F1]] | +0.87 | +0.81 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[FANCA]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | STRING 718 |
| [[CENPM]] | +0.85 | +0.83 / +0.86 | both halves | 7e-06 | STRING 835 |
| [[TK1]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | STRING 572 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GINS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises GINS2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without E2F8 | 0.068 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises GINS2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without TCF19 | 0.079 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises GINS2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.94× lower at baseline in the lines without E2F2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises GINS2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CDC25A | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.883). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.4, -45.0); signed map (-37.9, -44.4). **Vector** length 94.2, 22.9% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *Cell Cycle Checkpoints* (reactome, mean cos +0.71 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.74 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +5.5 | +13.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +5.1 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.5 | +10.2 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.4 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +2.7 | +4.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -3.5 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -2.8 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GINS complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:85,676,198-85,690,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSF2, Pfs2 |
| Gene groups (HGNC) | GINS complex |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, G2M_CHECKPOINT |
| Reactome | 7 pathways, smallest: Unwinding of DNA; DNA strand elongation; Synthesis of DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y248](https://www.uniprot.org/uniprotkb/Q9Y248) (DNA replication complex GINS protein PSF2):

> Required for correct functioning of the GINS complex, a complex that plays an essential role in the initiation of DNA replication, and progression of DNA replication forks. GINS complex is a core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built.

**Summary**, from NCBI Gene [51659](https://www.ncbi.nlm.nih.gov/gene/51659):

> The yeast heterotetrameric GINS complex is made up of Sld5 (GINS4; MIM 610611), Psf1 (GINS1; MIM 610608), Psf2, and Psf3 (GINS3; MIM 610610). The formation of this complex is essential for the initiation of DNA replication in yeast and Xenopus egg extracts (Ueno et al., 2005 [PubMed 16287864]). See GINS1 for additional information about the GINS complex.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24575) · Entrez [51659](https://www.ncbi.nlm.nih.gov/gene/51659) · UniProt [Q9Y248](https://www.uniprot.org/uniprotkb/Q9Y248) · Ensembl [ENSG00000131153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131153)

## Data

Gene col 5179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5179); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5179]; `tensor/DDL_lfc|DDL_z.npy` [5179]; `embed/gene_vectors.npy` [5179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5179 or target_col == 5179). Every well: [[GINS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GINS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
