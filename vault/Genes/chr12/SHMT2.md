---
symbol: "SHMT2"
type: "gene"
col: 11259
ensembl_id: "ENSG00000182199"
name: "serine hydroxymethyltransferase 2"
location: "12q13.3"
module: 63
arm: "+"
pooled_cpm: 27.46
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SHMT2

*serine hydroxymethyltransferase 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +13.2, q 8e-37, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.48× (z +4.3, q 0.002, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.625× (z -7.3, q 1e-10, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS1]] (+0.76, fdr 7e-06), [[XPOT]] (+0.76, fdr 7e-06), [[TCEA1]] (+0.73, fdr 7e-06); moves opposite to [[POLR2L]] (-0.61, fdr 2e-05), [[TMEM50A]] (-0.47, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.32×** | +13.2 | 8e-37 | 37/42 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +10.9 | 2e-25 | 28/35 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.8 | 1e-12 | 32/40 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +5.2 | 3e-05 | 37/47 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.7 | 3e-04 | 29/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.002 | 25/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.04×** | +4.1 | 0.003 | 31/47 (NCI-H23, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.003 | 23/46 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.0 | 0.005 | 23/45 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.005 | 23/46 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.012 | 18/45 (A-427, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.021 | 18/48 (BT-474, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.022 | 20/47 (A549, CFPAC-1, …) | two highest doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.82×** | +3.4 | 0.023 | 17/46 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.023 | 20/48 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.70×** | +3.0 | 0.083 | 13/45 (NCI-H23, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -7.3 | 1e-10 | 27/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -4.6 | 0.001 | 25/48 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -4.4 | 0.002 | 27/46 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -4.3 | 0.002 | 27/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -4.2 | 0.002 | 23/46 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.043 | 22/46 (hTERT-HPNE, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -3.5 | 0.043 | 24/48 (LS 180, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 58.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 66.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.8) |
| [[A-172 (line)]] | wt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 27.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.0) |
| [[HT-29 (line)]] | alt | 69.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.8) |
| [[SW480 (line)]] | alt | 60.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -16.4) |
| [[HCT15 (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.1) |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.0) |
| [[RKO (line)]] | wt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.7) |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -9.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS1]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | STRING 454 |
| [[XPOT]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[TCEA1]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[IARS1]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 | STRING 509 |
| [[NARS1]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[TRIB3]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 534 |
| [[AARS1]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 | STRING 506 |
| [[PSAT1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 916 |
| [[PHGDH]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 926 |
| [[HSPA9]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 492 |
| [[PCK2]] | +0.68 | +0.60 / +0.74 | both halves | 7e-06 | STRING 562 |
| [[YARS1]] | +0.68 | +0.60 / +0.73 | both halves | 7e-06 | STRING 655 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2L]] | -0.61 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[TMEM50A]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 47.1); signed map (-14.3, 24.1). **Vector** length 89.9, 22.1% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.60 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.68 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.68 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.0 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +3.7 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +1.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | +0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | serine hydroxymethyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,229,573-57,234,935 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mSHMT; previously SHMT |
| Gene groups (HGNC) | Serine hydroxymethyltransferase family |
| Hallmark sets | XENOBIOTIC_METABOLISM, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Metabolism of folate and pterines; RHOG GTPase cycle; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P34897](https://www.uniprot.org/uniprotkb/P34897) (Serine hydroxymethyltransferase, mitochondrial):

> Catalyzes the cleavage of serine to glycine accompanied with the production of 5,10-methylenetetrahydrofolate, an essential intermediate for purine biosynthesis. Serine provides the major source of folate one-carbon in cells by catalyzing the transfer of one carbon from serine to tetrahydrofolate. Contributes to the de novo mitochondrial thymidylate biosynthesis pathway via its role in glycine and tetrahydrofolate metabolism: thymidylate biosynthesis is required to prevent uracil accumulation …

**Summary**, from NCBI Gene [6472](https://www.ncbi.nlm.nih.gov/gene/6472):

> This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes the cytosolic form of this enzyme is located on chromosome 17. Alternative splicing results in …

**Accessions** — [HGNC:10852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10852) · Entrez [6472](https://www.ncbi.nlm.nih.gov/gene/6472) · UniProt [P34897](https://www.uniprot.org/uniprotkb/P34897) · Ensembl [ENSG00000182199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182199)

## Data

Gene col 11259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11259); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11259]; `tensor/DDL_lfc|DDL_z.npy` [11259]; `embed/gene_vectors.npy` [11259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11259 or target_col == 11259). Every well: [[SHMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
