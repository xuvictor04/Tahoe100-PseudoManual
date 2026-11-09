---
symbol: "IFRD2"
type: "gene"
col: 13214
ensembl_id: "ENSG00000214706"
name: "interferon related developmental regulator 2"
location: "3p21.31"
module: 1
arm: "+"
pooled_cpm: 9.58
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# IFRD2

*interferon related developmental regulator 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.64× (z +11.0, q 2e-25, up in 25 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.97× (z +7.7, q 2e-12, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.716× (z -5.4, q 4e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP4]] (+0.82, fdr 7e-06), [[BYSL]] (+0.78, fdr 7e-06), [[PSMG1]] (+0.77, fdr 7e-06); moves opposite to [[GNAS]] (-0.69, fdr 7e-06), [[TMEM59]] (-0.67, fdr 7e-06), [[APTR]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.64×** | +11.0 | 2e-25 | 25/31 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +9.0 | 8e-17 | 16/21 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.31×** | +7.9 | 6e-13 | 10/17 (NCI-H460, A498, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.97×** | +7.7 | 2e-12 | 32/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.60×** | +7.6 | 5e-12 | 21/43 (NCI-H2347, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.17×** | +7.3 | 4e-11 | 33/44 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +6.7 | 1e-09 | 28/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +6.0 | 2e-07 | 25/45 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.69×** | +5.9 | 2e-07 | 18/38 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.0 | 3e-05 | 22/41 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.67×** | +4.8 | 9e-05 | 19/37 (HS-578T, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.3 | 1e-03 | 16/35 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.001 | 16/45 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.95×** | +4.0 | 0.003 | 12/44 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +3.9 | 0.004 | 14/46 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.004 | 15/45 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.012 | 11/46 (HOP62, NCI-H2347, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.017 | 12/46 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.76×** | +3.3 | 0.024 | 10/37 (NCI-H2030, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.025 | 8/42 (H4, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.043 | 5/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +3.0 | 0.056 | 8/41 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -5.4 | 4e-05 | 21/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.5 | 0.002 | 19/43 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.682×** | -4.4 | 0.002 | 20/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.766× | -3.1 | 0.31 | 11/45 (AN3 CA, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 22.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.430× (z -8.5) |
| [[SW480 (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.48× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.17 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +8.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.166× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 9.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +11.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -11.1) |
| [[SW48 (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP4]] | +0.82 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[BYSL]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[PSMG1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[MAK16]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[RRS1]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[POGK]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[TRMT61A]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | STRING 571 |
| [[PGAM5]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ATIC]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[UTP15]] | +0.71 | +0.66 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.69 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[APTR]] | -0.62 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SERF2]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, -38.8); signed map (-2.6, -43.8). **Vector** length 77.2, 15.8% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.58 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.60 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.61 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.6 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.4 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | interferon related developmental regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,287,732-50,292,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKMc15, SM15, IFNRP |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12894](https://www.uniprot.org/uniprotkb/Q12894) (Interferon-related developmental regulator 2):

> Ribosome-binding protein that acts as an inhibitor of mRNA translation by promoting ribosome inactivation. Associates with the P- and E-sites of the ribosome and inserts a C-terminal helix into the mRNA exit channel to preclude translation (By similarity).

**Summary**, from NCBI Gene [7866](https://www.ncbi.nlm.nih.gov/gene/7866):

> Enables ribosome binding activity and translation repressor activity. Involved in negative regulation of translation. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5457) · Entrez [7866](https://www.ncbi.nlm.nih.gov/gene/7866) · UniProt [Q12894](https://www.uniprot.org/uniprotkb/Q12894) · Ensembl [ENSG00000214706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214706)

## Data

Gene col 13214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13214); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13214]; `tensor/DDL_lfc|DDL_z.npy` [13214]; `embed/gene_vectors.npy` [13214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13214 or target_col == 13214). Every well: [[IFRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
