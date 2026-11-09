---
symbol: "UPF1"
type: "gene"
col: 61
ensembl_id: "ENSG00000005007"
name: "UPF1 RNA helicase and ATPase"
location: "19p13.11"
module: 36
arm: "+"
pooled_cpm: 31.64
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# UPF1

*UPF1 RNA helicase and ATPase* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.35× (z +14.4, q 4e-44, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.0866×, SW48 0.123×, LoVo 0.359×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.127×, SW48 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.212×, SHP-77 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-423 0.294×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD1A]] (+0.73, fdr 7e-06), [[DDX23]] (+0.70, fdr 7e-06), [[MLLT1]] (+0.63, fdr 8e-06); moves opposite to [[ABI1]] (-0.56, fdr 1e-05), [[CERT1]] (-0.54, fdr 4e-05), [[CHMP2B]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 61.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.35×** | +14.4 | 4e-44 | 45/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +11.2 | 1e-26 | 37/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +11.0 | 6e-26 | 38/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.9 | 6e-13 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 7e-13 | 29/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.8 | 7e-13 | 33/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +7.6 | 2e-12 | 25/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +7.4 | 7e-12 | 30/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.38×** | +7.3 | 3e-11 | 26/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +6.7 | 1e-09 | 27/48 (HS-578T, Hs 766T, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.6 | 1e-06 | 26/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.28×** | +5.4 | 4e-06 | 20/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +5.3 | 6e-06 | 24/48 (HS-578T, HOP62, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +5.3 | 6e-06 | 21/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.1 | 1e-05 | 24/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +5.0 | 2e-05 | 18/48 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.008 | 13/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +2.9 | 0.076 | 8/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 61.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.0866×, SW48 0.123×, LoVo 0.359×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 0.127×, SW48 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.212×, SHP-77 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (SNU-423 0.294×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.845× | -3.8 | 0.071 | 13/48 (A498, HS-578T, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.856× | -3.6 | 0.11 | 8/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | 0.864× | -3.3 | 0.16 | 3/47 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.16 | 9/47 (HT-29, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 61. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 53.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.11× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 40.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 38.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.29× (z +11.1) | — |
| [[A498 (line)]] | wt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 37.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[KATO III (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 43.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.78× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0866× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 61.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.43× (z +8.6) | — |
| [[RKO (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 28.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.294× (z -9.3) |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0688× (z -9.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 61), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD1A]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[DDX23]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MLLT1]] | +0.63 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[CHERP]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC5]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 | STRING 663 |
| [[TRRAP]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PCNX3]] | +0.59 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[CSK]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RANBP3]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[POLR3H]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF384]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[E2F4]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[CERT1]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CHMP2B]] | -0.52 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[MEF2A]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SLC41A2]] | -0.50 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.3, -10.0); signed map (-10.7, -28.6). **Vector** length 72.0, 12.7% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +11.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +14.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | +4.0 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +1.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.3 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | UPF1 RNA helicase and ATPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,831,959-18,868,230 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUPF1, KIAA0221, NORF1, pNORF1, smg-2; previously RENT1 |
| Gene groups (HGNC) | UPF1 like RNA helicases; SURF complex; DECID complex |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC); Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92900](https://www.uniprot.org/uniprotkb/Q92900) (Regulator of nonsense transcripts 1):

> RNA-dependent helicase required for nonsense-mediated decay (NMD) of aberrant mRNAs containing premature stop codons and which modulates the expression level of normal mRNAs. ATP-dependent 5'-3' helicase active on RNA:DNA substrates with a 5'-RNA extension. ATP-dependent 5'-3' helicase active on RNA:RNA substrates with a 5'-RNA extension. ATP-dependent 5'-3' helicase active on DNA:DNA substrates with a 5'-DNA extension. Is recruited to mRNAs upon translation termination and undergoes a cycle of …

**Summary**, from NCBI Gene [5976](https://www.ncbi.nlm.nih.gov/gene/5976):

> This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons. This protein is located only in the cytoplasm. When translation ends, it interacts with the …

**Accessions** — [HGNC:9962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9962) · Entrez [5976](https://www.ncbi.nlm.nih.gov/gene/5976) · UniProt [Q92900](https://www.uniprot.org/uniprotkb/Q92900) · Ensembl [ENSG00000005007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005007)

## Data

Gene col 61: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 61); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 61, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 61]; `tensor/DDL_lfc|DDL_z.npy` [61]; `embed/gene_vectors.npy` [61]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 61 or target_col == 61). Every well: [[UPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
