---
symbol: "LRRC47"
type: "gene"
col: 5120
ensembl_id: "ENSG00000130764"
name: "leucine rich repeat containing 47"
location: "1p36.32"
module: 107
arm: "+"
pooled_cpm: 19.39
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# LRRC47

*leucine rich repeat containing 47* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.63× (z +9.3, q 6e-18, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.749× (z -8.3, q 6e-14, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.112×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (H4 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRMS1]] (+0.65, fdr 7e-06), [[PTPN23]] (+0.64, fdr 8e-06), [[COASY]] (+0.64, fdr 7e-06); moves opposite to [[ARHGAP26]] (-0.51, fdr 2e-05), [[PEAK1]] (-0.51, fdr 2e-05), [[CCDC88A]] (-0.50, fdr 4e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +9.3 | 6e-18 | 33/48 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +9.1 | 2e-17 | 33/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +9.1 | 2e-17 | 32/44 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.52×** | +8.5 | 2e-15 | 28/48 (SW480, PANC-1, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +7.8 | 9e-13 | 26/46 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.4 | 2e-11 | 32/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +6.2 | 4e-08 | 24/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +6.0 | 2e-07 | 19/48 (PANC-1, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +5.5 | 2e-06 | 19/44 (NCI-H1792, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 4e-06 | 21/47 (NCI-H1792, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.1 | 2e-05 | 15/48 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.3 | 8e-04 | 11/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.23×** | +4.1 | 0.002 | 16/40 (SNU-423, A-172, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.23×** | +4.1 | 0.002 | 16/46 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.24×** | +4.0 | 0.002 | 13/37 (SW1417, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.016 | 4/48 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.016 | 8/48 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.019 | 7/47 (J82, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.028 | 5/48 (SW 900, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.069 | 8/46 (AsPC-1, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5120.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.112×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.271×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (H4 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -8.3 | 6e-14 | 32/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.762×** | -5.5 | 9e-06 | 22/48 (NCI-H2347, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Gemcitabine (drug)]] 0.5 µM |  | 0.842× | -3.5 | 0.074 | 10/48 (HCT15, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.846× | -3.3 | 0.15 | 7/47 (C32, SW48, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.863× | -3.0 | 0.29 | 10/45 (AN3 CA, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.263× (z -8.5) ⚠ toxic |
| [[H4 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -12.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRMS1]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PTPN23]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[COASY]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SLC25A38]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[SAMM50]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[XAB2]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TMEM11]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TADA2B]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ZNF142]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[DDX49]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP26]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PEAK1]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CCDC88A]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TMSB4X]] | -0.50 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[CD83]] | -0.50 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -3.6); signed map (-11.1, -26.2). **Vector** length 70.1, 11.4% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.3 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,778,559-3,796,498 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1185, RP1-286D6.3 |
| Matched by | ensembl_id |

UniProt [Q8N1G4](https://www.uniprot.org/uniprotkb/Q8N1G4) carries no function annotation.

**Summary**, from NCBI Gene [57470](https://www.ncbi.nlm.nih.gov/gene/57470):

> Enables RNA binding activity. Predicted to be involved in phenylalanyl-tRNA aminoacylation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29207) · Entrez [57470](https://www.ncbi.nlm.nih.gov/gene/57470) · UniProt [Q8N1G4](https://www.uniprot.org/uniprotkb/Q8N1G4) · Ensembl [ENSG00000130764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130764)

## Data

Gene col 5120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5120); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5120]; `tensor/DDL_lfc|DDL_z.npy` [5120]; `embed/gene_vectors.npy` [5120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5120 or target_col == 5120). Every well: [[LRRC47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
