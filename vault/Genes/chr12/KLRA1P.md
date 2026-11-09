---
symbol: "KLRA1P"
type: "gene"
col: 15002
ensembl_id: "ENSG00000256667"
name: "killer cell lectin like receptor A1, pseudogene"
location: "12p13.2"
module: 37
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# KLRA1P

*killer cell lectin like receptor A1, pseudogene* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +7.5, q 2e-11, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.531× (z -6.7, q 9e-09, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAS2R4]] (+0.79, fdr 7e-06), [[LINC01355]] (+0.75, fdr 7e-06), [[SMIM15-AS1]] (+0.75, fdr 7e-06); moves opposite to [[KCTD17]] (-0.63, fdr 6e-05), [[PAFAH1B3]] (-0.62, fdr 2e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.5 | 2e-11 | 21/38 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +6.4 | 5e-08 | 22/44 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.3 | 6e-08 | 3/11 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.6 | 3e-06 | 11/23 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.3 | 1e-05 | 12/38 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.2 | 2e-05 | 14/38 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.7 | 2e-04 | 1/4 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.5 | 5e-04 | 4/8 (A498, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 9e-04 | 11/38 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.001 | 8/45 (H4, A498, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.009 | 10/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.013 | 12/35 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.014 | 7/43 (C-33 A, NCI-H2030, …) | rises with dose | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.014 | 1/46 (A498) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.76×** | +3.1 | 0.068 | 1/46 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -6.7 | 9e-09 | 20/44 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.564×** | -6.1 | 3e-07 | 20/44 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.579×** | -5.8 | 1e-06 | 17/36 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.588×** | -5.7 | 2e-06 | 22/44 (SW480, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.585×** | -5.5 | 5e-06 | 17/43 (MIA PaCa-2, LS 180, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.617×** | -5.1 | 3e-05 | 16/46 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.650×** | -4.6 | 3e-04 | 15/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -4.0 | 0.004 | 8/45 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.515×** | -3.7 | 0.014 | 7/32 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -3.6 | 0.015 | 10/38 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.522×** | -3.6 | 0.015 | 13/40 (NCI-H1573, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.720×** | -3.5 | 0.021 | 13/45 (NCI-H1573, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.712×** | -3.4 | 0.026 | 5/42 (NCI-H1573, SW480, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -3.3 | 0.035 | 8/45 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -3.2 | 0.051 | 9/43 (SNU-423, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -3.2 | 0.057 | 12/44 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 0.05 µM |  | **0.736×** | -3.0 | 0.081 | 10/41 (C-33 A, hTERT-HPNE, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0745× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 6.92 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -9.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H23 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.0) | — |
| [[SW480 (line)]] | alt | 4.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R4]] | +0.79 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[LINC01355]] | +0.75 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.75 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[MSH4]] | +0.75 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.75 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.74 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[CASS4]] | +0.74 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[RRH]] | +0.74 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ARL9]] | +0.73 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.73 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[SMG1P7]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.71 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD17]] | -0.63 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[PAFAH1B3]] | -0.62 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLRA1P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, -16.6); signed map (14.2, 6.2). **Vector** length 68.2, 10.5% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor A1, pseudogene |
| Locus type | pseudogene |
| Location | 12p13.2 — chr12:10,589,386-10,598,209 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | Ly49, LY49L; previously KLRA1, KLRAP1 |
| Gene groups (HGNC) | Killer cell lectin like receptors; Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:6372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6372) · Entrez [10748](https://www.ncbi.nlm.nih.gov/gene/10748) · Ensembl [ENSG00000256667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256667)

## Data

Gene col 15002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15002); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15002]; `tensor/DDL_lfc|DDL_z.npy` [15002]; `embed/gene_vectors.npy` [15002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15002 or target_col == 15002). Every well: [[KLRA1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRA1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
