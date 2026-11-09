---
symbol: "EIF6"
type: "gene"
col: 14314
ensembl_id: "ENSG00000242372"
name: "eukaryotic translation initiation factor 6"
location: "20q11.22"
module: 1
arm: "+"
pooled_cpm: 29.92
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# EIF6

*eukaryotic translation initiation factor 6* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +9.1, q 8e-17, up in 38 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.87× (z +6.9, q 1e-09, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.315×, AsPC-1 0.339×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7A]] (+0.74, fdr 7e-06), [[NIP7]] (+0.72, fdr 7e-06), [[ZNF562]] (+0.71, fdr 7e-06); moves opposite to [[GNAS]] (-0.65, fdr 9e-06), [[PTMA]] (-0.61, fdr 1e-05), [[RCN2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.27×** | +9.1 | 8e-17 | 38/46 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +6.9 | 1e-09 | 43/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.81×** | +6.3 | 5e-08 | 35/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.78×** | +6.2 | 1e-07 | 24/32 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.3 | 1e-05 | 35/46 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.3 | 1e-05 | 30/47 (HT-29, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.74×** | +5.1 | 2e-05 | 30/39 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.5 | 4e-04 | 25/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 27/48 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.42×** | +3.9 | 0.006 | 25/44 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.009 | 25/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.023 | 21/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.023 | 26/47 (SK-MEL-2, BT-474, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.38×** | +3.4 | 0.023 | 22/45 (J82, Panc 03.27, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.036 | 20/47 (BT-474, HT-29, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.051 | 20/47 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.061 | 16/48 (HT-29, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14314.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.315×, AsPC-1 0.339×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.724× | -3.1 | 0.76 | 20/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.17× (z +11.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.65× (z +9.3) | — |
| [[A498 (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A549 (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 46.9 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.05× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7A]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 | same gene group |
| [[NIP7]] | +0.72 | +0.70 / +0.77 | both halves | 7e-06 | same gene group; STRING 985 |
| [[ZNF562]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[FADD]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[JMJD4]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[IFRD2]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BYSL]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 | STRING 446 |
| [[FLAD1]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[COA4]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RPF1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 | same gene group; STRING 983 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.65 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[PTMA]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[RCN2]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SLC25A40]] | -0.58 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | -0.58 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[USP33]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[H3-3A]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NUCB2]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.56 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[USF2]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[TXNDC16]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PTMS]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-45.1, 0.5); signed map (2.5, -45.1). **Vector** length 70.0, 16.5% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,278,907-35,284,985 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p27BBP, b(2)gcn; previously EIF3A, ITGB4BP |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P56537](https://www.uniprot.org/uniprotkb/P56537) (Eukaryotic translation initiation factor 6):

> Binds to the 60S ribosomal subunit and prevents its association with the 40S ribosomal subunit to form the 80S initiation complex in the cytoplasm. Behaves as a stimulatory translation initiation factor downstream insulin/growth factors. Is also involved in ribosome biogenesis. Associates with pre-60S subunits in the nucleus and is involved in its nuclear export. Cytoplasmic release of TIF6 from 60S subunits and nuclear relocalization is promoted by a RACK1 (RACK1)-dependent protein kinase C …

**Summary**, from NCBI Gene [3692](https://www.ncbi.nlm.nih.gov/gene/3692):

> Hemidesmosomes are structures which link the basal lamina to the intermediate filament cytoskeleton. An important functional component of hemidesmosomes is the integrin beta-4 subunit (ITGB4), a protein containing two fibronectin type III domains. The protein encoded by this gene binds to the fibronectin type III domains of ITGB4 and may help link ITGB4 to the intermediate filament cytoskeleton. The encoded protein, which is insoluble and found both in the nucleus and in the cytoplasm, can …

**Accessions** — [HGNC:6159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6159) · Entrez [3692](https://www.ncbi.nlm.nih.gov/gene/3692) · UniProt [P56537](https://www.uniprot.org/uniprotkb/P56537) · Ensembl [ENSG00000242372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242372)

## Data

Gene col 14314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14314); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14314]; `tensor/DDL_lfc|DDL_z.npy` [14314]; `embed/gene_vectors.npy` [14314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14314 or target_col == 14314). Every well: [[EIF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
