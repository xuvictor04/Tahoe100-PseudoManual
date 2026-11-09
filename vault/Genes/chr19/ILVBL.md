---
symbol: "ILVBL"
type: "gene"
col: 2550
ensembl_id: "ENSG00000105135"
name: "2-hydroxyacyl-CoA lyase 2"
location: "19p13.12"
module: 17
arm: "+"
pooled_cpm: 10.76
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ILVBL

*2-hydroxyacyl-CoA lyase 2* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.44× (z +4.8, q 8e-04, up in 19 of 42 measured lines) ⚠ transcription drop. The strongest without an alert is [[Bimiralisib (drug)]] 0.5 µM: 1.44× (z +3.4, q 0.068, up in 7 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.419× (z -16.3, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKIPSD]] (+0.59, fdr 1e-05), [[EDC4]] (+0.56, fdr 4e-05), [[PSRC1]] (+0.56, fdr 3e-05); moves opposite to [[BMAL2-AS1]] (-0.55, fdr 2e-05), [[PDK1-AS1]] (-0.53, fdr 2e-04), [[RASSF8-AS1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.8 | 8e-04 | 19/42 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.058 | 1/48 (HOP62) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.068 | 7/22 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.64×** | +3.4 | 0.068 | 6/44 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.068 | 7/44 (A549, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -16.3 | 0e+00 | 41/45 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.494×** | -9.3 | 2e-18 | 39/47 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.480×** | -9.3 | 2e-18 | 33/46 (C-33 A, SW48, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.608×** | -9.3 | 2e-18 | 28/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.500×** | -9.1 | 7e-18 | 37/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.522×** | -8.6 | 8e-16 | 33/47 (A498, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -8.4 | 3e-15 | 32/46 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -8.1 | 5e-14 | 30/44 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.531×** | -8.0 | 5e-14 | 30/46 (NCI-H2030, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -8.0 | 5e-14 | 31/47 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.569×** | -7.4 | 5e-12 | 29/46 (LS 180, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.597×** | -6.8 | 4e-10 | 26/46 (BT-474, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -6.2 | 3e-08 | 28/47 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -5.9 | 2e-07 | 27/47 (H4, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.643×** | -5.8 | 2e-07 | 24/47 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.639×** | -5.7 | 5e-07 | 26/45 (A498, NCI-H2030, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.638×** | -5.6 | 7e-07 | 24/46 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -5.5 | 2e-06 | 25/47 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 24.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.6) |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0874× (z -21.1) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.4) |
| [[A498 (line)]] | wt | 16.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -11.6) |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 9.79 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.6) |
| [[HOP62 (line)]] | alt | 9.51 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -9.0) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.9) |
| [[SW48 (line)]] | wt | 14.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0747× (z -10.4) |
| [[A-172 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 8.18 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0689× (z -9.4) |
| [[C32 (line)]] | wt | 8.71 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.0) |
| [[H4 (line)]] | wt | 18.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.138× (z -8.8) |
| [[HT-29 (line)]] | alt | 5.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -8.6) |
| [[LoVo (line)]] | wt | 6.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.5) |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0607× (z -11.8) |
| [[SNU-423 (line)]] | alt | 9.20 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.8) |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 8.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.4) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKIPSD]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[EDC4]] | +0.56 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[PSRC1]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PIP4P1]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[MADD]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PRPF39]] | +0.53 | +0.35 / +0.42 | both halves | 1e-04 |  |
| [[ALDOC]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[MTMR4]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[EFNA4]] | +0.52 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[SLC26A6]] | +0.51 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[OSBPL7]] | +0.51 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[CEP192]] | +0.51 | +0.48 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMAL2-AS1]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PDK1-AS1]] | -0.53 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[RASSF8-AS1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[OMG]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TMLHE-AS1]] | -0.51 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[SMCO2]] | -0.50 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[LINC01829]] | -0.50 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ZNF561-AS1]] | -0.50 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[TPTE2P6]] | -0.50 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[EHBP1-AS1]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[STMP1]] | -0.49 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[AADACL2-AS1]] | -0.49 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ILVBL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.2, -57.3); signed map (-7.5, 20.3). **Vector** length 65.9, 10.8% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.7 | -9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.6 | -8.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -16.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | 2-hydroxyacyl-CoA lyase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,114,984-15,125,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 209L8, AHAS, ILV2H, MGC1269, FLJ39061, MGC19535, HACL1L, HACL2; previously ILVBL |
| Gene groups (HGNC) | Flavoproteins; 2-hydroxyacyl-CoA lyase family |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L0T0](https://www.uniprot.org/uniprotkb/A1L0T0) (2-hydroxyacyl-CoA lyase 2):

> Endoplasmic reticulum 2-OH acyl-CoA lyase involved in the cleavage (C1 removal) reaction in the fatty acid alpha-oxydation in a thiamine pyrophosphate (TPP)-dependent manner. Involved in the phytosphingosine degradation pathway.

**Summary**, from NCBI Gene [10994](https://www.ncbi.nlm.nih.gov/gene/10994):

> The protein encoded by this gene shares similarity with several thiamine pyrophosphate-binding proteins identified in bacteria, yeast, and plants. The highest degree of similarity is found with bacterial acetolactate synthases (AHAS), which are enzymes that catalyze the first step in branched-chain amino acid biosynthesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6041) · Entrez [10994](https://www.ncbi.nlm.nih.gov/gene/10994) · UniProt [A1L0T0](https://www.uniprot.org/uniprotkb/A1L0T0) · Ensembl [ENSG00000105135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105135)

## Data

Gene col 2550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2550); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2550]; `tensor/DDL_lfc|DDL_z.npy` [2550]; `embed/gene_vectors.npy` [2550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2550 or target_col == 2550). Every well: [[ILVBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILVBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
