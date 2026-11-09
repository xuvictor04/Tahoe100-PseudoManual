---
symbol: "ZNF23"
type: "gene"
col: 9458
ensembl_id: "ENSG00000167377"
name: "zinc finger protein 23"
location: "16q22.2"
module: 11
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZNF23

*zinc finger protein 23* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +12.9, q 2e-35, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.420× (z -13.6, q 2e-39, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.483× (z -11.4, q 1e-27, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL58]] (+0.74, fdr 7e-06), [[GORAB]] (+0.71, fdr 7e-06), [[REXO4]] (+0.71, fdr 7e-06); moves opposite to [[CMPK1]] (-0.63, fdr 7e-06), [[STT3B]] (-0.60, fdr 7e-06), [[TMED4]] (-0.60, fdr 9e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL9]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +12.9 | 2e-35 | 32/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +11.0 | 9e-26 | 33/42 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +10.5 | 1e-23 | 29/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +10.5 | 2e-23 | 44/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +10.3 | 8e-23 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +8.7 | 3e-16 | 34/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +8.1 | 5e-14 | 29/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +6.4 | 1e-08 | 27/47 (A-172, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.2 | 3e-08 | 20/48 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 2e-07 | 24/47 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +5.7 | 6e-07 | 25/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +5.4 | 2e-06 | 19/44 (SNU-423, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 9e-05 | 20/45 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.7 | 1e-04 | 22/47 (A-172, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 9/43 (PANC-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.003 | 12/47 (A498, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -13.6 | 2e-39 | 36/45 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.483×** | -11.4 | 1e-27 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -10.3 | 1e-22 | 33/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -8.5 | 2e-15 | 35/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -5.9 | 4e-07 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -4.8 | 2e-04 | 20/41 (SNU-423, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.767×** | -4.2 | 0.003 | 17/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.819× | -3.1 | 0.12 | 12/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.758× | -3.1 | 0.12 | 4/47 (HCT15, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.5 | 2 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.219× (z -11.4) |
| [[A-172 (line)]] | wt | 19.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +14.5) | — |
| [[A498 (line)]] | wt | 15.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -15.8) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -11.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.225× (z -8.8) |
| [[BT-474 (line)]] | alt | 8.80 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Menadione (drug)]] 0.05 µM 0.105× (z -8.9) |
| [[C32 (line)]] | wt | 13.6 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0728× (z -13.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 19.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0795× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -12.4) |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -10.8) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 9.83 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0986× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0721× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.114× (z -9.3) |
| [[J82 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.1) | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.80× (z +10.1) ⚠ toxic | — |
| [[RKO (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.9) ⚠ cell-cycle shift, explains ~7% of this change |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | +0.74 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[GORAB]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[REXO4]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[SURF6]] | +0.70 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.70 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.69 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | same gene group |
| [[PHAX]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.68 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.68 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[RBAK]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.63 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[STT3B]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMED4]] | -0.60 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[PHTF2]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.59 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.57 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.57 | -0.60 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL9]] | C | KLHL9 activity lowers ZNF23's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without KLHL9 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.7, 4.1); signed map (-0.3, -22.1). **Vector** length 79.4, 15.0% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +8.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,447,597-71,463,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX16, Zfp612, ZNF612; previously ZNF359 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17027](https://www.uniprot.org/uniprotkb/P17027) (Zinc finger protein 23):

> May be involved in transcriptional regulation. May have a role in embryonic development.

**Summary**, from NCBI Gene [7571](https://www.ncbi.nlm.nih.gov/gene/7571):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13023) · Entrez [7571](https://www.ncbi.nlm.nih.gov/gene/7571) · UniProt [P17027](https://www.uniprot.org/uniprotkb/P17027) · Ensembl [ENSG00000167377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167377)

## Data

Gene col 9458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9458); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9458]; `tensor/DDL_lfc|DDL_z.npy` [9458]; `embed/gene_vectors.npy` [9458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9458 or target_col == 9458). Every well: [[ZNF23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
