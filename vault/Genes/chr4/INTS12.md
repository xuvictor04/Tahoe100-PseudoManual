---
symbol: "INTS12"
type: "gene"
col: 6239
ensembl_id: "ENSG00000138785"
name: "integrator complex subunit 12"
location: "4q24"
module: 28
arm: "+"
pooled_cpm: 24.92
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# INTS12

*integrator complex subunit 12* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +30.4, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Larotrectinib (drug)]] 0.5 µM in 1 line (CHP-212 0.0754×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM128]] (+0.66, fdr 1e-05), [[ZSCAN21]] (+0.63, fdr 3e-05), [[GIN1]] (+0.62, fdr 5e-05); moves opposite to [[KANK2]] (-0.55, fdr 1e-04), [[LMBR1]] (-0.55, fdr 5e-05), [[OSBPL8]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +30.4 | 0e+00 | 45/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +24.3 | 0e+00 | 44/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +19.1 | 0e+00 | 43/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.08×** | +17.5 | 0e+00 | 45/48 (LS 180, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +16.2 | 0e+00 | 42/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +12.5 | 7e-34 | 36/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +12.4 | 3e-33 | 40/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +11.9 | 1e-30 | 38/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +10.5 | 8e-24 | 39/48 (SW 900, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.5 | 8e-24 | 37/48 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.3 | 8e-19 | 34/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.1 | 2e-14 | 28/46 (AsPC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +7.4 | 7e-12 | 25/48 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.1 | 5e-11 | 28/48 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +6.4 | 7e-09 | 24/47 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 2e-07 | 21/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Larotrectinib (drug)]] 0.5 µM in 1 line (CHP-212 0.0754×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Naproxen (drug)]] 0.05 µM |  | 0.855× | -3.5 | 0.20 | 8/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.20 | 9/48 (NCI-H23, SW 1271, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.876× | -3.2 | 0.27 | 6/47 (C-33 A, KATO III, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 36.4 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +16.3) | — |
| [[SW480 (line)]] | alt | 19.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.9) | — |
| [[LoVo (line)]] | wt | 31.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +37.4) | — |
| [[PANC-1 (line)]] | alt | 22.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +25.0) | — |
| [[AsPC-1 (line)]] | alt | 36.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +27.2) | — |
| [[HT-29 (line)]] | alt | 26.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +21.3) | — |
| [[NCI-H2347 (line)]] | alt | 28.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +20.4) | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +26.0) | — |
| [[A549 (line)]] | wt | 22.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 38.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +24.6) | — |
| [[HEC-1-A (line)]] | alt | 28.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +17.4) | — |
| [[HOP62 (line)]] | alt | 20.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.6) | — |
| [[KATO III (line)]] | alt | 21.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.5) | — |
| [[SW48 (line)]] | wt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +11.3) | — |
| [[A-427 (line)]] | wt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +17.9) | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0754× (z -9.3) |
| [[COLO 205 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +13.8) | — |
| [[J82 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +16.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +19.0) | — |
| [[SW 900 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +17.6) | — |
| [[SW1417 (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.5) | — |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM128]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ZSCAN21]] | +0.63 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[GIN1]] | +0.62 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[SMIM19]] | +0.61 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[COQ5]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ELAC1]] | +0.59 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[KCTD18]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ZNF777]] | +0.59 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[SUPT20H]] | +0.58 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MTMR6]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[IFT74]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANK2]] | -0.55 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[LMBR1]] | -0.55 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[OSBPL8]] | -0.50 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[RRP7BP-1]] | -0.49 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[CEP72]] | -0.49 | -0.51 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.9, 6.8); signed map (7.1, -23.5). **Vector** length 69.9, 13.1% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +24.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +17.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +16.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +12.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.6 | +10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -2.2 | +4.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -2.0 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,682,627-105,895,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SBBI22, INT12; previously PHF22 |
| Gene groups (HGNC) | PHD finger proteins; Integrator complex |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CB8](https://www.uniprot.org/uniprotkb/Q96CB8) (Integrator complex subunit 12):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [57117](https://www.ncbi.nlm.nih.gov/gene/57117):

> INTS12 is a subunit of the Integrator complex, which associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690) (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25067) · Entrez [57117](https://www.ncbi.nlm.nih.gov/gene/57117) · UniProt [Q96CB8](https://www.uniprot.org/uniprotkb/Q96CB8) · Ensembl [ENSG00000138785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138785)

## Data

Gene col 6239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6239); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6239]; `tensor/DDL_lfc|DDL_z.npy` [6239]; `embed/gene_vectors.npy` [6239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6239 or target_col == 6239). Every well: [[INTS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
