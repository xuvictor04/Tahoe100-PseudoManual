---
symbol: "HSD17B3"
type: "gene"
col: 5148
ensembl_id: "ENSG00000130948"
name: "hydroxysteroid 17-beta dehydrogenase 3"
location: "9q22.32"
module: 26
arm: "+"
pooled_cpm: 6.53
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# HSD17B3

*hydroxysteroid 17-beta dehydrogenase 3* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +9.9, q 2e-20, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.404× (z -6.9, q 2e-09, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.303× (z -4.8, q 2e-04, down in 21 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP70]] (+0.82, fdr 7e-06), [[PSMD7-DT]] (+0.82, fdr 7e-06), [[MGAM]] (+0.81, fdr 7e-06); moves opposite to [[L2HGDH]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLCO1B1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +9.9 | 2e-20 | 34/41 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.17×** | +8.7 | 9e-16 | 30/45 (LoVo, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +6.7 | 4e-09 | 3/12 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +5.8 | 1e-06 | 23/37 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.05×** | +5.4 | 7e-06 | 21/44 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **3.65×** | +5.2 | 2e-05 | 25/42 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +4.8 | 2e-04 | 9/18 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.77×** | +4.3 | 0.001 | 16/45 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.006 | 18/44 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +3.6 | 0.017 | 9/30 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.028 | 10/38 (SNU-1, SW480, …) | all doses, flat | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **2.35×** | +3.4 | 0.029 | 9/44 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 16/46 (J82, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +3.3 | 0.046 | 11/44 (A498, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.053 | 8/45 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.053 | 15/45 (HepG2/C3A, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.066 | 12/45 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.080 | 18/39 (LoVo, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.404×** | -6.9 | 2e-09 | 34/45 (NCI-H1573, SW1417, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.469×** | -5.7 | 3e-06 | 24/45 (KATO III, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.485×** | -5.5 | 8e-06 | 25/45 (KATO III, NCI-H1573, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.303×** | -4.8 | 2e-04 | 21/35 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.338×** | -4.3 | 0.002 | 21/42 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.363×** | -4.1 | 0.004 | 17/38 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.617×** | -3.7 | 0.021 | 20/40 (LoVo, NCI-H2030, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.627×** | -3.6 | 0.024 | 19/43 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -3.5 | 0.025 | 18/45 (NCI-H23, HT-29, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.559×** | -3.2 | 0.080 | 7/45 (SW 900, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.671× | -3.1 | 0.11 | 16/45 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.668× | -3.1 | 0.11 | 16/45 (COLO 205, SW 1271, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.676× | -3.0 | 0.11 | 18/45 (NCI-H460, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 39.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 11.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.4× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.0682× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[A-172 (line)]] | wt | 4.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0653× (z -8.9) |
| [[J82 (line)]] | alt | 4.17 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 3.62 | 0 | 1 | — | [[Diphenhydramine (drug)]] 5 µM 0.0553× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 2.08 | 0 | 1 | — | [[Simotinib (drug)]] 0.5 µM 0.0681× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 3.67 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.109× (z -8.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-427 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP70]] | +0.82 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.82 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MGAM]] | +0.81 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[NEB]] | +0.81 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.79 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.77 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.77 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.77 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[LINC01762]] | +0.77 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.77 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.77 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.76 | +0.73 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.65 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1B1]] | B | SLCO1B1 activity raises HSD17B3's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without SLCO1B1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.6, 17.1); signed map (23.2, -0.3). **Vector** length 89.4, 18.2% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +4.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.3 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.0 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -3.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 17-beta dehydrogenase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:96,235,306-96,302,176 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR12C2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 7 pathways, smallest: Androgen biosynthesis; Synthesis of very long-chain fatty acyl-CoAs; Metabolism of steroid hormones |
| Matched by | ensembl_id |

**Function**, from UniProt [P37058](https://www.uniprot.org/uniprotkb/P37058) (17-beta-hydroxysteroid dehydrogenase type 3):

> Catalyzes the conversion of 17-oxosteroids to 17beta-hydroxysteroids. Favors the reduction of androstenedione to testosterone. Testosterone is the key androgen driving male development and function. Uses NADPH while the two other EDH17B enzymes use NADH. Androgens such as epiandrosterone, dehydroepiandrosterone, androsterone and androstanedione are accepted as substrates and reduced at C-17. Can reduce 11-ketoandrostenedione as well as 11beta-hydroxyandrostenedione at C-17 to the respective …

**Summary**, from NCBI Gene [3293](https://www.ncbi.nlm.nih.gov/gene/3293):

> This isoform of 17 beta-hydroxysteroid dehydrogenase is expressed predominantly in the testis and catalyzes the conversion of androstenedione to testosterone. It preferentially uses NADP as cofactor. Deficiency can result in male pseudohermaphroditism with gynecomastia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5212) · Entrez [3293](https://www.ncbi.nlm.nih.gov/gene/3293) · UniProt [P37058](https://www.uniprot.org/uniprotkb/P37058) · Ensembl [ENSG00000130948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130948)

## Data

Gene col 5148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5148); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5148]; `tensor/DDL_lfc|DDL_z.npy` [5148]; `embed/gene_vectors.npy` [5148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5148 or target_col == 5148). Every well: [[HSD17B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
