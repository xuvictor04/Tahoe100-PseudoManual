---
symbol: "IER3IP1"
type: "gene"
col: 5502
ensembl_id: "ENSG00000134049"
name: "immediate early response 3 interacting protein 1"
location: "18q21.1"
module: 40
arm: "+"
pooled_cpm: 58.67
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IER3IP1

*immediate early response 3 interacting protein 1* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +5.2, q 1e-04, up in 28 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.69× (z +4.1, q 0.006, up in 27 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.443× (z -17.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP1]] (+0.83, fdr 7e-06), [[PRRC1]] (+0.80, fdr 7e-06), [[GPR107]] (+0.79, fdr 7e-06); moves opposite to [[CMTR2]] (-0.66, fdr 1e-05), [[ZNF518A]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.62×** | +5.2 | 1e-04 | 28/48 (SK-MEL-2, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.35×** | +4.5 | 0.002 | 28/48 (SHP-77, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.33×** | +4.1 | 0.006 | 24/43 (SW480, SHP-77, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.006 | 27/49 (A498, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.006 | 23/49 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.32×** | +3.8 | 0.015 | 25/45 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.28×** | +3.7 | 0.019 | 22/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +3.6 | 0.019 | 17/48 (BT-474, Panc 03.27, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.040 | 20/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.26×** | +3.4 | 0.044 | 23/47 (NCI-H23, Hs 766T, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.2 | 0.072 | 18/48 (A-427, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | 1.22× | +3.0 | 0.12 | 20/47 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.443×** | -17.0 | 0e+00 | 46/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.533×** | -9.0 | 1e-16 | 41/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -8.1 | 1e-13 | 39/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -4.2 | 0.003 | 26/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.762×** | -3.9 | 0.013 | 26/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -3.7 | 0.019 | 23/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.5 | 0.032 | 22/47 (BT-474, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.2 | 0.095 | 18/48 (A498, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 95.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -24.6) |
| [[A-172 (line)]] | wt | 41.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 92.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -19.5) |
| [[A498 (line)]] | wt | 82.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.4) |
| [[C-33 A (line)]] | alt | 72.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.4) |
| [[H4 (line)]] | wt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.4) |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.4) |
| [[HS-578T (line)]] | alt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.8) |
| [[LoVo (line)]] | wt | 62.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 55.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 54.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 80.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 72.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.0) |
| [[SW480 (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.1) |
| [[A-427 (line)]] | wt | 49.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.3) |
| [[HCT15 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0623× (z -9.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.4) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.2) |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 86.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.5) |
| [[J82 (line)]] | alt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.3) |
| [[KATO III (line)]] | alt | 69.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 86.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 63.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.2) |
| [[SNU-1 (line)]] | wt | 78.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.6) |
| [[SNU-423 (line)]] | alt | 36.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.4) |
| [[SW 1088 (line)]] | alt | 92.2 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0978× (z -8.6) |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.0) |
| [[SW1417 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.3) |
| [[A549 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | +0.83 | +0.85 / +0.74 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.80 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[GPR107]] | +0.79 | +0.83 / +0.73 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.79 | +0.85 / +0.78 | both halves | 7e-06 | STRING 434 |
| [[TMEM39A]] | +0.79 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.78 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[COG6]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.77 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[COG5]] | +0.76 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.76 | +0.79 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTR2]] | -0.66 | -0.72 / -0.56 | both halves | 1e-05 |  |
| [[ZNF518A]] | -0.65 | -0.67 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.863). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.8, -31.8); signed map (-49.1, 9.0). **Vector** length 120, 37.2% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.1 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.2 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.4 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | immediate early response 3 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:47,152,834-47,176,364 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5U9](https://www.uniprot.org/uniprotkb/Q9Y5U9) (Immediate early response 3-interacting protein 1):

> Regulator of endoplasmic reticulum secretion that acts as a key determinant of brain size. Required for secretion of extracellular matrix proteins. Required for correct brain development by depositing sufficient extracellular matrix proteins for tissue integrity and the proliferation of neural progenitors. Acts as a regulator of the unfolded protein response (UPR) (By similarity).

**Summary**, from NCBI Gene [51124](https://www.ncbi.nlm.nih.gov/gene/51124):

> This gene encodes a small protein that is localized to the endoplasmic reticulum (ER) and may play a role in the ER stress response by mediating cell differentiation and apoptosis. Transcription of this gene is regulated by tumor necrosis factor alpha and specificity protein 1 (Sp1). Mutations in this gene may play a role in microcephaly, epilepsy, and diabetes syndrome (MEDS), and a pseudogene of this gene is located on the long arm of chromosome 12. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:18550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18550) · Entrez [51124](https://www.ncbi.nlm.nih.gov/gene/51124) · UniProt [Q9Y5U9](https://www.uniprot.org/uniprotkb/Q9Y5U9) · Ensembl [ENSG00000134049](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134049)

## Data

Gene col 5502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5502); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5502]; `tensor/DDL_lfc|DDL_z.npy` [5502]; `embed/gene_vectors.npy` [5502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5502 or target_col == 5502). Every well: [[IER3IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IER3IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
