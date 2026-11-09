---
symbol: "SRP54"
type: "gene"
col: 2034
ensembl_id: "ENSG00000100883"
name: "signal recognition particle 54"
location: "14q13.2"
module: 41
arm: "+"
pooled_cpm: 227.55
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SRP54

*signal recognition particle 54* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.37× (z +8.3, q 4e-14, up in 46 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (PANC-1 7.13×, COLO 205 7.16×, Panc 03.27 3.90×, LoVo 6.00×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 3.23×, SNU-423 2.17×; ⚠ cell-cycle shift, explains ~10% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 3.48×; ⚠ cell-cycle shift, explains ~5% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.461× (z -9.8, q 7e-20, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.652× (z -5.4, q 9e-06, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.90, fdr 7e-06), [[DNAJC25]] (+0.84, fdr 7e-06), [[EIF2AK3]] (+0.84, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2034.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (PANC-1 7.13×, COLO 205 7.16×, Panc 03.27 3.90×, LoVo 6.00×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 3.23×, SNU-423 2.17×; ⚠ cell-cycle shift, explains ~10% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 3.48×; ⚠ cell-cycle shift, explains ~5% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.37×** | +8.3 | 4e-14 | 46/49 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +4.9 | 2e-04 | 36/48 (LS 180, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -9.8 | 7e-20 | 42/44 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.483×** | -8.8 | 3e-16 | 43/45 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -6.1 | 2e-07 | 44/49 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.652×** | -5.4 | 9e-06 | 39/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.693×** | -4.4 | 0.001 | 35/48 (SW1417, CFPAC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.718×** | -3.9 | 0.007 | 33/49 (RPMI-7951, SW1417, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.720×** | -3.9 | 0.007 | 33/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.730×** | -3.7 | 0.013 | 30/48 (Panc 03.27, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -3.7 | 0.013 | 27/47 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.734×** | -3.7 | 0.013 | 36/49 (H4, SW1417, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -3.6 | 0.018 | 28/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.746×** | -3.5 | 0.023 | 34/49 (LS 180, H4, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.748×** | -3.5 | 0.023 | 34/49 (NCI-H2122, KATO III, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.4 | 0.023 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.755×** | -3.3 | 0.029 | 29/49 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.775×** | -3.3 | 0.029 | 31/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.033 | 29/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.835× | -3.1 | 0.057 | 21/48 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.644×** | -3.0 | 0.071 | 24/49 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 312 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 309 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 420 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 289 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +10.8) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.13× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 320 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 218 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 352 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 154 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.9) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[RPMI-7951 (line)]] | alt | 332 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 204 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 263 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 239 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.483× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 198 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.16× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 262 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 201 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.19× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 234 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.90× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 204 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.5) ⚠ cell-cycle shift, explains ~10% of this change | — |
| [[SW1417 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 248 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 181 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 397 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 264 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 227 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 166 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 792 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.90 | +0.90 / +0.87 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[COG6]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[PGM3]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | STRING 416 |
| [[SEC31A]] | +0.80 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.79 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[COPB1]] | +0.79 | +0.83 / +0.72 | both halves | 7e-06 | STRING 681 |
| [[DPM1]] | +0.79 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[COPA]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.79 | +0.75 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.65 | -0.72 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.867). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.9, -34.9); signed map (-50.6, 12.2). **Vector** length 151, 63.9% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.56 to 12); *Asparagine N-linked glycosylation* (reactome, mean cos +0.58 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.8 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.3 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -0.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.3 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.9 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.4 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | signal recognition particle 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:34,981,957-35,029,686 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Signal recognition particle; Signal recognition particle GTPases |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P61011](https://www.uniprot.org/uniprotkb/P61011) (Signal recognition particle subunit SRP54):

> Component of the signal recognition particle (SRP) complex, a ribonucleoprotein complex that mediates the cotranslational targeting of secretory and membrane proteins to the endoplasmic reticulum (ER). As part of the SRP complex, associates with the SRP receptor (SR) component SRPRA to target secretory proteins to the endoplasmic reticulum membrane. Binds to the signal sequence of presecretory proteins when they emerge from the ribosomes. Displays basal GTPase activity, and stimulates …

**Summary**, from NCBI Gene [6729](https://www.ncbi.nlm.nih.gov/gene/6729):

> Enables several functions, including 7S RNA binding activity; endoplasmic reticulum signal peptide binding activity; and guanyl ribonucleotide binding activity. Contributes to GTPase activity. Involved in granulocyte differentiation and protein targeting to ER. Located in cytoplasm and nucleus. Part of signal recognition particle, endoplasmic reticulum targeting. Implicated in severe congenital neutropenia 8. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11301) · Entrez [6729](https://www.ncbi.nlm.nih.gov/gene/6729) · UniProt [P61011](https://www.uniprot.org/uniprotkb/P61011) · Ensembl [ENSG00000100883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100883)

## Data

Gene col 2034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2034); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2034]; `tensor/DDL_lfc|DDL_z.npy` [2034]; `embed/gene_vectors.npy` [2034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2034 or target_col == 2034). Every well: [[SRP54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRP54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
