---
symbol: "TIMM8A"
type: "gene"
col: 4782
ensembl_id: "ENSG00000126953"
name: "translocase of inner mitochondrial membrane 8A"
location: "Xq22.1"
module: 33
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TIMM8A

*translocase of inner mitochondrial membrane 8A* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 14.7× (z +23.3, q 0e+00, up in 22 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.79× (z +5.0, q 3e-05, up in 16 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.149×; ⚠ cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0769×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGAM5]] (+0.67, fdr 7e-06), [[MRPL4]] (+0.66, fdr 7e-06), [[EXOSC2]] (+0.64, fdr 7e-06); moves opposite to [[SMIM14]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 21 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **14.7×** | +23.3 | 0e+00 | 22/22 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **17.2×** | +21.2 | 0e+00 | 9/9 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **11.3×** | +19.4 | 0e+00 | 12/12 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.06×** | +8.3 | 1e-14 | 20/24 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.50×** | +7.9 | 3e-13 | 38/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.31×** | +7.2 | 4e-11 | 32/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.12×** | +6.5 | 7e-09 | 23/34 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.92×** | +5.6 | 1e-06 | 25/46 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.0 | 3e-05 | 16/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.79×** | +5.0 | 3e-05 | 15/37 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +5.0 | 3e-05 | 23/46 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.88×** | +4.7 | 1e-04 | 12/29 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +4.4 | 5e-04 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.002 | 15/44 (SW1417, CFPAC-1, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.58×** | +3.9 | 0.003 | 8/25 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 15/45 (SK-MEL-2, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.30×** | +3.8 | 0.006 | 9/42 (PANC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.10×** | +3.3 | 0.022 | 7/32 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.06×** | +3.3 | 0.027 | 3/33 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.029 | 13/45 (NCI-H460, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.035 | 14/46 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.00×** | +3.1 | 0.036 | 1/26 (RKO) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.64×** | +3.0 | 0.046 | 6/45 (A498, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.0 | 0.051 | 6/33 (NCI-H460, RKO, …) | all doses, flat | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.056 | 9/43 (HS-578T, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.056 | 7/43 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.43×** | +2.9 | 0.056 | 4/45 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.057 | 5/45 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.149×; ⚠ cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.633× | -3.7 | 0.11 | 10/46 (A-427, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.661× | -3.1 | 0.29 | 7/46 (SW1417, J82, …) | top dose only | plate-row cell shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.682× | -3.1 | 0.29 | 5/46 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.510× | -3.1 | 0.29 | 7/43 (C-33 A, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.779× | -3.0 | 0.29 | 10/45 (SW480, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.62 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.5× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 2.85 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 54.0× (z +12.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 5.85 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 8.90 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.0× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.62 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.3× (z +13.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.99 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.1× (z +12.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 10.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.01× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 7.62 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0769× (z -10.4) |
| [[HS-578T (line)]] | alt | 1.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.5× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 5.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.6× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 3.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 36.1× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 4.74 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.7× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 4.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.2× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM5]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MRPL4]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[CISD3]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[BOP1]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[WDR77]] | +0.62 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[NME1]] | +0.61 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DCTPP1]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALKBH2]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PFAS]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.0, -41.8); signed map (-10.6, -52.6). **Vector** length 50.8, 7.35% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +23.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +21.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +19.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,345,661-101,348,742 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDP, MTS; previously DFN1 |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O60220](https://www.uniprot.org/uniprotkb/O60220) (Mitochondrial import inner membrane translocase subunit Tim8 A):

> Mitochondrial intermembrane chaperone that participates in the import and insertion of some multi-pass transmembrane proteins into the mitochondrial inner membrane. Also required for the transfer of beta-barrel precursors from the TOM complex to the sorting and assembly machinery (SAM complex) of the outer membrane. Acts as a chaperone-like protein that protects the hydrophobic precursors from aggregation and guide them through the mitochondrial intermembrane space. The TIMM8-TIMM13 complex …

**Summary**, from NCBI Gene [1678](https://www.ncbi.nlm.nih.gov/gene/1678):

> This translocase is involved in the import and insertion of hydrophobic membrane proteins from the cytoplasm into the mitochondrial inner membrane. The gene is mutated in Mohr-Tranebjaerg syndrome/Deafness Dystonia Syndrome (MTS/DDS) and it is postulated that MTS/DDS is a mitochondrial disease caused by a defective mitochondrial protein import system. Defects in this gene also cause Jensen syndrome; an X-linked disease with opticoacoustic nerve atrophy and muscle weakness. This protein, along …

**Accessions** — [HGNC:11817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11817) · Entrez [1678](https://www.ncbi.nlm.nih.gov/gene/1678) · UniProt [O60220](https://www.uniprot.org/uniprotkb/O60220) · Ensembl [ENSG00000126953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126953)

## Data

Gene col 4782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4782); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4782]; `tensor/DDL_lfc|DDL_z.npy` [4782]; `embed/gene_vectors.npy` [4782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4782 or target_col == 4782). Every well: [[TIMM8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
