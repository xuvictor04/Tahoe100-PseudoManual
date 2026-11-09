---
symbol: "MUL1"
type: "gene"
col: 1622
ensembl_id: "ENSG00000090432"
name: "mitochondrial E3 ubiquitin protein ligase 1"
location: "1p36.12"
module: 7
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MUL1

*mitochondrial E3 ubiquitin protein ligase 1* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.11× (z +15.2, q 0e+00, up in 44 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.0973×, HepG2/C3A 0.117×, NCI-H2030 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0689×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0892×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (RKO 0.0789×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-427 0.0826×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP14]] (+0.69, fdr 1e-05), [[LAMTOR1]] (+0.68, fdr 7e-06), [[RBM42]] (+0.68, fdr 7e-06); moves opposite to [[NAP1L1]] (-0.54, fdr 1e-05), [[CBX3]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.11×** | +15.2 | 0e+00 | 44/45 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +11.9 | 6e-30 | 35/41 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.27×** | +11.2 | 6e-27 | 29/41 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +8.9 | 5e-17 | 24/43 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +8.6 | 1e-15 | 12/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +7.6 | 2e-12 | 22/46 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.5 | 8e-12 | 22/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.2 | 5e-11 | 20/46 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.9 | 4e-10 | 20/45 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +6.8 | 6e-10 | 24/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 4e-07 | 19/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.7 | 8e-07 | 11/24 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 13/47 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 3e-05 | 13/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +5.0 | 3e-05 | 15/47 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 1e-04 | 12/43 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.001 | 13/48 (Hs 766T, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.007 | 8/41 (Hs 766T, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1622.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW1417 0.0973×, HepG2/C3A 0.117×, NCI-H2030 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0689×); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0892×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (RKO 0.0789×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-427 0.0826×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.9 | 0.053 | 10/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.817× | -3.3 | 0.24 | 9/45 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | 0.811× | -3.2 | 0.24 | 8/44 (A549, SW480, …) | inconsistent across doses | position effect removed |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.24 | 8/45 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 8.49 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0689× (z -12.6) |
| [[A-427 (line)]] | wt | 4.32 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0826× (z -8.5) |
| [[A498 (line)]] | wt | 7.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0892× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 8.45 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 8.22 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.120× (z -9.4) ⚠ toxic |
| [[RKO (line)]] | wt | 9.57 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0789× (z -10.9) |
| [[A-172 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP14]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[LAMTOR1]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RBM42]] | +0.68 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ZNF136]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[KTI12]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.62 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MRPS18A]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZSWIM1]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZNF594]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MOCS3]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L1]] | -0.54 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[CBX3]] | -0.53 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.4, 11.1); signed map (-1.2, -24.3). **Vector** length 58.9, 8.50% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +11.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | +0.3 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,499,448-20,508,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12875, MULAN, RNF218, MAPL, GIDE; previously C1orf166 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 7 pathways, smallest: KEAP1-NFE2L2 pathway; Ub-specific processing proteases; Cellular response to chemical stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969V5](https://www.uniprot.org/uniprotkb/Q969V5) (Mitochondrial ubiquitin ligase activator of NFKB 1):

> E3 ubiquitin-protein ligase activity, which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates. Can ubiquitinate AKT1 preferentially at 'Lys-284' involving 'Lys-48'-linked polyubiquitination and seems to be involved in regulation of Akt signaling by targeting phosphorylated Akt to proteasomal degradation. Mediates polyubiquitination of cytoplasmic p53/TP53 at 'Lys-24' which targets TP53 for …

**Summary**, from NCBI Gene [79594](https://www.ncbi.nlm.nih.gov/gene/79594):

> Enables several functions, including p53 binding activity; ubiquitin protein ligase binding activity; and ubiquitin-like protein transferase activity. Involved in several processes, including cellular response to exogenous dsRNA; negative regulation of defense response; and regulation of mitochondrion organization. Located in several cellular components, including mitochondrial outer membrane; neuronal cell body; and peroxisome. Part of TOM complex. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:25762](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25762) · Entrez [79594](https://www.ncbi.nlm.nih.gov/gene/79594) · UniProt [Q969V5](https://www.uniprot.org/uniprotkb/Q969V5) · Ensembl [ENSG00000090432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090432)

## Data

Gene col 1622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1622); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1622]; `tensor/DDL_lfc|DDL_z.npy` [1622]; `embed/gene_vectors.npy` [1622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1622 or target_col == 1622). Every well: [[MUL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
