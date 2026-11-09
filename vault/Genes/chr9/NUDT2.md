---
symbol: "NUDT2"
type: "gene"
col: 9049
ensembl_id: "ENSG00000164978"
name: "nudix hydrolase 2"
location: "9p13.3"
module: 30
arm: "+"
pooled_cpm: 9.87
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# NUDT2

*nudix hydrolase 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +8.4, q 2e-14, up in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.19×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 4.48×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -13.6, q 4e-39, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HINFP]] (+0.71, fdr 7e-06), [[ASB7]] (+0.70, fdr 7e-06), [[MZT2A]] (+0.70, fdr 7e-06); moves opposite to [[CSRP1]] (-0.69, fdr 1e-05), [[SLC35A4]] (-0.59, fdr 3e-05), [[MTNR1A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9049.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.19×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 4.48×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.4 | 2e-14 | 25/44 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +7.7 | 3e-12 | 23/39 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.2 | 3e-05 | 19/46 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +4.0 | 0.009 | 15/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.8 | 0.016 | 6/27 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.23× | +3.2 | 0.12 | 6/47 (KATO III, LS 180, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.12 | 11/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 4/47 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 13/43 (A549, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.12 | 5/41 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.539×** | -13.6 | 4e-39 | 39/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -9.0 | 4e-17 | 27/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.589×** | -8.2 | 4e-14 | 27/44 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -7.2 | 7e-11 | 26/48 (SW480, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.729×** | -4.9 | 1e-04 | 16/45 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -4.7 | 2e-04 | 17/37 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.9 | 0.008 | 12/47 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.813× | -3.2 | 0.11 | 13/46 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.808× | -3.0 | 0.15 | 4/47 (CHP-212, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.4) |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.2) |
| [[SW480 (line)]] | alt | 10.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 9.31 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0736× (z -13.9) |
| [[A498 (line)]] | wt | 9.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -9.8) |
| [[COLO 205 (line)]] | alt | 8.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -9.3) |
| [[KATO III (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HINFP]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ASB7]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[MZT2A]] | +0.70 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[TAF11]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD42-DT]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[WDR20]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.65 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.65 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[NENF]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[KIAA2013]] | +0.64 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[TCTN3]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.69 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.59 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[MTNR1A]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[LINC00460]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ARHGDIA]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CELSR3]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.56 | -0.38 / -0.64 | both halves | 6e-05 |  |
| [[NAB1]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[WDR1]] | -0.55 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DST]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-12.4, 23.6); signed map (-23.8, -0.8). **Vector** length 65.1, 9.99% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.3 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,329,506-34,343,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously APAH1 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 4 pathways, smallest: Detoxification of Reactive Oxygen Species; Cellular response to chemical stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P50583](https://www.uniprot.org/uniprotkb/P50583) (Bis(5'-nucleosyl)-tetraphosphatase):

> Catalyzes the asymmetric hydrolysis of diadenosine 5',5'''-P1,P4-tetraphosphate (Ap4A) to yield AMP and ATP (By similarity). Exhibits decapping activity towards FAD-capped RNAs and dpCoA-capped RNAs in vitro (By similarity).

**Summary**, from NCBI Gene [318](https://www.ncbi.nlm.nih.gov/gene/318):

> This gene encodes a member of the MutT family of nucleotide pyrophosphatases, a subset of the larger NUDIX hydrolase family. The gene product possesses a modification of the MutT sequence motif found in certain nucleotide pyrophosphatases. The enzyme asymmetrically hydrolyzes Ap4A to yield AMP and ATP and is responsible for maintaining the intracellular level of the dinucleotide Ap4A, the function of which has yet to be established. This gene may be a candidate tumor suppressor gene. …

**Accessions** — [HGNC:8049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8049) · Entrez [318](https://www.ncbi.nlm.nih.gov/gene/318) · UniProt [P50583](https://www.uniprot.org/uniprotkb/P50583) · Ensembl [ENSG00000164978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164978)

## Data

Gene col 9049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9049); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9049]; `tensor/DDL_lfc|DDL_z.npy` [9049]; `embed/gene_vectors.npy` [9049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9049 or target_col == 9049). Every well: [[NUDT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
