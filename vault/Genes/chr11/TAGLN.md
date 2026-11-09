---
symbol: "TAGLN"
type: "gene"
col: 7394
ensembl_id: "ENSG00000149591"
name: "transgelin"
location: "11q23.3"
module: 39
arm: "+"
pooled_cpm: 7.47
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TAGLN

*transgelin* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.64× (z +16.8, q 0e+00, up in 12 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +14.0, q 2e-42, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.566× (z -7.7, q 7e-12, down in 24 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.630× (z -6.3, q 1e-07, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.69, fdr 1e-05), [[NLGN3]] (+0.68, fdr 1e-05), [[C3orf20]] (+0.68, fdr 1e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +16.8 | 0e+00 | 12/13 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +16.6 | 0e+00 | 26/29 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +15.6 | 0e+00 | 16/21 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +14.0 | 2e-42 | 25/39 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.2 | 6e-11 | 21/41 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.6 | 3e-09 | 14/40 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.3 | 8e-06 | 13/40 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 7/47 (HT-29, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.024 | 5/46 (A-427, A-172, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.024 | 10/41 (NCI-H23, SNU-423, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.024 | 3/41 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.069 | 5/44 (BT-474, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.079 | 9/46 (A-172, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.089 | 6/43 (KATO III, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -7.7 | 7e-12 | 24/41 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -6.3 | 1e-07 | 20/46 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.634×** | -6.2 | 1e-07 | 19/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -4.6 | 4e-04 | 16/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -4.6 | 4e-04 | 17/46 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -4.3 | 0.001 | 16/46 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.709×** | -4.3 | 0.002 | 10/45 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.8 | 0.009 | 10/43 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -3.8 | 0.010 | 15/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.010 | 12/45 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.043 | 9/46 (SW48, SW 900, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.783×** | -3.3 | 0.043 | 8/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.636×** | -3.2 | 0.058 | 8/28 (HepG2/C3A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 32.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +9.3) | — |
| [[LoVo (line)]] | wt | 5.39 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +9.3) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0663× (z -11.9) |
| [[SNU-423 (line)]] | alt | 18.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 7.12 | 0 | 2 (1 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.0774× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 5.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0858× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0590× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0786× (z -10.4) ⚠ cell-cycle shift, explains ~12% of this change |
| [[Hs 766T (line)]] | wt | 6.30 | 0 | 1 | — | [[Demeclocycline (drug)]] 0.05 µM 0.0576× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 3.85 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0966× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0796× (z -9.3) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H2347 (line)]] | alt | 2.57 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0755× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 8.80 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0877× (z -8.7) |
| [[A-172 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.69 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.68 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.68 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[TMEM25]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[C21orf91-OT1]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[BTG3-AS1]] | +0.66 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[AVIL]] | +0.65 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[TTC36]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.65 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -14.1); signed map (18.1, 6.6). **Vector** length 76.8, 12.9% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | transgelin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:117,199,370-117,207,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SM22, WS3-10, TAGLN1, SMCC, DKFZp686P11128, TGLN |
| Gene groups (HGNC) | Transgelin family |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01995](https://www.uniprot.org/uniprotkb/Q01995) (Transgelin):

> Actin cross-linking/gelling protein (By similarity). Involved in calcium interactions and contractile properties of the cell that may contribute to replicative senescence.

**Summary**, from NCBI Gene [6876](https://www.ncbi.nlm.nih.gov/gene/6876):

> This gene encodes a shape change and transformation sensitive actin-binding protein which belongs to the calponin family. It is ubiquitously expressed in vascular and visceral smooth muscle, and is an early marker of smooth muscle differentiation. The encoded protein is thought to be involved in calcium-independent smooth muscle contraction. It acts as a tumor suppressor, and the loss of its expression is an early event in cell transformation and the development of some tumors, coinciding with …

**Accessions** — [HGNC:11553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11553) · Entrez [6876](https://www.ncbi.nlm.nih.gov/gene/6876) · UniProt [Q01995](https://www.uniprot.org/uniprotkb/Q01995) · Ensembl [ENSG00000149591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149591)

## Data

Gene col 7394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7394); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7394]; `tensor/DDL_lfc|DDL_z.npy` [7394]; `embed/gene_vectors.npy` [7394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7394 or target_col == 7394). Every well: [[TAGLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAGLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
