---
symbol: "NANP"
type: "gene"
col: 9914
ensembl_id: "ENSG00000170191"
name: "N-acetylneuraminic acid phosphatase"
location: "20p11.21"
module: 1
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NANP

*N-acetylneuraminic acid phosphatase* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.34× (z +14.1, q 2e-42, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.753× (z -4.7, q 0.001, down in 13 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (Hs 766T 0.142×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.135×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2D]] (+0.59, fdr 1e-05), [[CHAMP1]] (+0.57, fdr 1e-05), [[UMPS]] (+0.55, fdr 1e-05); moves opposite to [[CSDE1]] (-0.56, fdr 3e-05), [[SPTBN1-AS2]] (-0.53, fdr 6e-05), [[ADNP-AS1]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.34×** | +14.1 | 2e-42 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.39×** | +13.9 | 1e-41 | 33/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +13.0 | 1e-36 | 30/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.97×** | +11.3 | 3e-27 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.90×** | +10.7 | 2e-24 | 34/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.87×** | +10.3 | 4e-23 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +10.0 | 9e-22 | 30/38 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +10.0 | 1e-21 | 30/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +7.8 | 3e-13 | 26/47 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +7.6 | 1e-12 | 27/47 (SW480, H4, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +7.1 | 6e-11 | 23/47 (HT-29, LOX-IMVI, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.42×** | +5.9 | 2e-07 | 15/47 (J82, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.7 | 4e-07 | 21/47 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.41×** | +5.7 | 4e-07 | 21/45 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.38×** | +5.3 | 5e-06 | 15/46 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 0.001 | 14/42 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.004 | 1/43 (Hs 766T) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.6 | 0.008 | 7/48 (Panc 03.27, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.021 | 5/48 (A549, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.14× | +3.1 | 0.043 | 4/48 (SHP-77, A498, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.054 | 2/41 (SK-MEL-2, SNU-1) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.084 | 3/45 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.13× | +2.8 | 0.097 | 1/48 (RPMI-7951) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9914.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.0906×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (Hs 766T 0.142×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.135×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.753×** | -4.7 | 0.001 | 13/47 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.4 | 0.003 | 4/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.839× | -4.2 | 0.006 | 7/48 (A549, NCI-H23, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.795×** | -3.8 | 0.018 | 12/46 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.879× | -3.1 | 0.24 | 7/48 (AN3 CA, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.20 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0906× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.135× (z -8.5) |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.142× (z -9.5) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2D]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.57 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[UMPS]] | +0.55 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SRRD]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[COA7]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PPIL1]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PINX1]] | +0.53 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FARSA]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ZNF770]] | +0.53 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MGA]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PANK3]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[EEFSEC]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSDE1]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SPTBN1-AS2]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[ADNP-AS1]] | -0.52 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[ST13]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[KDELR1]] | -0.51 | -0.46 / -0.59 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[RPL22]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[PCBP2]] | -0.49 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[PPHLN1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GNAS]] | -0.49 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ALDH2]] | -0.48 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SEZ6L2]] | -0.48 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | C | NANP's natural level lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | NANP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.041 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.6, 0.3); signed map (3.2, -37.6). **Vector** length 58.1, 7.88% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +1.5 |

## What is on record

|  |  |
|---|---|
| Name | N-acetylneuraminic acid phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,612,935-25,624,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ694B14.3, MGC26833; previously C20orf147, HDHD4 |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases; Haloacid dehalogenase like hydrolase domain containing |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBE9](https://www.uniprot.org/uniprotkb/Q8TBE9) (N-acylneuraminate-9-phosphatase):

> Catalyzes the dephosphorylation of N-acylneuraminate 9-phosphate (Neu5Ac-9-P) to N-acetylneuraminic acid (Neu5Ac or sialic acid). Can also use N-glycoloylneuraminate 9-phosphate as substrate.

**Summary**, from NCBI Gene [140838](https://www.ncbi.nlm.nih.gov/gene/140838):

> Enables N-acylneuraminate-9-phosphatase activity. Involved in CMP-N-acetylneuraminate biosynthetic process and N-acetylneuraminate biosynthetic process. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16140) · Entrez [140838](https://www.ncbi.nlm.nih.gov/gene/140838) · UniProt [Q8TBE9](https://www.uniprot.org/uniprotkb/Q8TBE9) · Ensembl [ENSG00000170191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170191)

## Data

Gene col 9914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9914); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9914]; `tensor/DDL_lfc|DDL_z.npy` [9914]; `embed/gene_vectors.npy` [9914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9914 or target_col == 9914). Every well: [[NANP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NANP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
