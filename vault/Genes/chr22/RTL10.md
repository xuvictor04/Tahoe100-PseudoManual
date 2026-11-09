---
symbol: "RTL10"
type: "gene"
col: 13238
ensembl_id: "ENSG00000215012"
name: "retrotransposon Gag like 10"
location: "22q11.21"
module: 3
arm: "+"
pooled_cpm: 12.54
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RTL10

*retrotransposon Gag like 10* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.15× (z +10.7, q 7e-24, up in 31 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.06× (z +10.5, q 3e-23, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.668× (z -8.2, q 1e-13, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNQ]] (+0.65, fdr 1e-05), [[DEXI]] (+0.65, fdr 7e-06), [[XYLT2]] (+0.62, fdr 3e-05); moves opposite to [[STAG2]] (-0.56, fdr 7e-05), [[TRIP12]] (-0.54, fdr 3e-04), [[RIPK2-DT]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +10.7 | 7e-24 | 31/40 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +10.5 | 3e-23 | 38/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +10.2 | 5e-22 | 42/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +9.7 | 4e-20 | 35/47 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.0 | 7e-05 | 20/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 2e-04 | 22/44 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +4.1 | 0.004 | 13/44 (Hs 766T, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.33×** | +3.9 | 0.005 | 19/45 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.9 | 0.005 | 7/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +3.7 | 0.012 | 6/47 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.19× | +3.5 | 0.021 | 10/48 (NCI-H23, Hs 766T, …) | rises with dose | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.024 | 9/46 (SK-MEL-2, COLO 205, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.030 | 10/42 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.032 | 9/48 (HT-29, hTERT-HPNE, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.036 | 10/48 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.036 | 6/45 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.039 | 7/46 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.049 | 9/46 (NCI-H1573, BT-474, …) | two highest doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.076 | 7/46 (H4, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.668×** | -8.2 | 1e-13 | 28/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -7.1 | 4e-10 | 22/46 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.604×** | -3.8 | 0.028 | 13/47 (Hs 766T, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.1) |
| [[A-172 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.2) |
| [[A498 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.0) |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0697× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 8.24 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0819× (z -8.6) |
| [[HOP62 (line)]] | alt | 9.41 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.166× (z -9.5) |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -8.9) |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.00× (z +9.0) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.193× (z -10.1) |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.3) |
| [[SW 900 (line)]] | alt | 7.68 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0695× (z -8.9) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.116× (z -9.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNQ]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[DEXI]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[XYLT2]] | +0.62 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SDHAF1]] | +0.62 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ZXDC]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[ANKS6]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CDAN1]] | +0.58 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TSEN54]] | +0.58 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[VKORC1L1]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[SAC3D1]] | +0.54 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[ZMYND19]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[XKR8]] | +0.54 | +0.36 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STAG2]] | -0.56 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[TRIP12]] | -0.54 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[RIPK2-DT]] | -0.54 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[CHD3]] | -0.53 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CLCN3]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[GDAP1]] | -0.52 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[ABCA10]] | -0.51 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[AMZ2P1]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[DZIP3]] | -0.50 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PLA2G6]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[GNGT1]] | -0.50 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MED12]] | -0.50 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.480). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-5.1, -18.4); signed map (-40.5, 0.6). **Vector** length 69.3, 11.3% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +10.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.2 | +4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +9.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | retrotransposon Gag like 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,846,138-19,854,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21125, BOP; previously C22orf29 |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only; Retrotransposon Gag like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L3V2](https://www.uniprot.org/uniprotkb/Q7L3V2) (Protein Bop):

> Could induce apoptosis in a BH3 domain-dependent manner. The direct interaction network of Bcl-2 family members may play a key role in modulation RTL10/BOP intrinsic apoptotic signaling activity.

**Summary**, from NCBI Gene [79680](https://www.ncbi.nlm.nih.gov/gene/79680):

> Involved in mitochondrial outer membrane permeabilization and regulation of mitochondrial membrane potential. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26112) · Entrez [79680](https://www.ncbi.nlm.nih.gov/gene/79680) · UniProt [Q7L3V2](https://www.uniprot.org/uniprotkb/Q7L3V2) · Ensembl [ENSG00000215012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215012)

## Data

Gene col 13238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13238); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13238]; `tensor/DDL_lfc|DDL_z.npy` [13238]; `embed/gene_vectors.npy` [13238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13238 or target_col == 13238). Every well: [[RTL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
