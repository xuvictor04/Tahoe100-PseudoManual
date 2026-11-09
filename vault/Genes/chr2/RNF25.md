---
symbol: "RNF25"
type: "gene"
col: 8698
ensembl_id: "ENSG00000163481"
name: "ring finger protein 25"
location: "2q35"
module: 7
arm: "+"
pooled_cpm: 6.11
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RNF25

*ring finger protein 25* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.15× (z +12.1, q 5e-31, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.593× (z -6.2, q 3e-07, down in 20 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Saquinavir (drug)]] 0.05 µM: 0.737× (z -3.7, q 0.070, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0974×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.5 µM in 1 line (LoVo 0.0537×; ⚠ transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0559×); [[Naproxen (drug)]] 0.05 µM in 1 line (SNU-423 0.0906×); [[Hesperidin (drug)]] 5 µM in 1 line (RPMI-7951 0.0800×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HARS2]] (+0.70, fdr 7e-06), [[ZNF408]] (+0.67, fdr 7e-06), [[ZSCAN22]] (+0.67, fdr 7e-06); moves opposite to [[PEAK1]] (-0.56, fdr 2e-05), [[ARIH1]] (-0.54, fdr 1e-05), [[CRY1]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8698.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.15×** | +12.1 | 5e-31 | 39/44 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +11.3 | 4e-27 | 29/40 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.82×** | +10.8 | 4e-25 | 31/41 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +10.4 | 4e-23 | 29/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +9.0 | 3e-17 | 34/45 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +7.5 | 4e-12 | 31/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.90×** | +7.1 | 1e-10 | 20/43 (A498, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +6.7 | 1e-09 | 24/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +6.2 | 4e-08 | 23/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +6.0 | 1e-07 | 22/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.9 | 2e-07 | 17/34 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +5.7 | 8e-07 | 17/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 23/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 2e-05 | 14/45 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.7 | 1e-04 | 13/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.005 | 4/45 (SHP-77, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8698.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.0974×; ⚠ toxic; transcription drop); [[Pimozide (drug)]] 0.5 µM in 1 line (LoVo 0.0537×; ⚠ transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Neratinib (maleate) (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0559×); [[Naproxen (drug)]] 0.05 µM in 1 line (SNU-423 0.0906×); [[Hesperidin (drug)]] 5 µM in 1 line (RPMI-7951 0.0800×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -6.2 | 3e-07 | 20/28 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 0.05 µM |  | **0.737×** | -3.7 | 0.070 | 14/43 (C-33 A, HCT15, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.750× | -3.5 | 0.10 | 11/46 (LS 180, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8698. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.61 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.8× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0974× (z -14.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.61 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0537× (z -11.6) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 4.83 | 0 | 1 | — | [[Neratinib (maleate) (drug)]] 0.05 µM 0.0559× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 5.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -11.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 7.73 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0800× (z -8.6) |
| [[SNU-423 (line)]] | alt | 5.83 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0906× (z -8.6) |
| [[A-172 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8698), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HARS2]] | +0.70 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ZNF408]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 | STRING 779 |
| [[ZSCAN22]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[EIF2B2]] | +0.67 | +0.77 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[ZNF613]] | +0.66 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[CBLL1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF211]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZNF225]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[KCTD10]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TRIM32]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ZSCAN25]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEAK1]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ARIH1]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | same gene group |
| [[CRY1]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.8, 4.1); signed map (-9.3, -25.2). **Vector** length 57.0, 7.71% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +12.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +3.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.3 | -6.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Tolcapone (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,663,892-218,672,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AO7, FLJ13906 |
| Gene groups (HGNC) | Ring finger proteins; RWD domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BH1](https://www.uniprot.org/uniprotkb/Q96BH1) (E3 ubiquitin-protein ligase RNF25):

> E3 ubiquitin-protein ligase that plays a key role in the RNF14-RNF25 translation quality control pathway, a pathway that takes place when a ribosome has stalled during translation, and which promotes ubiquitination and degradation of translation factors on stalled ribosomes. Catalyzes ubiquitination of RPS27A in response to ribosome collisions, promoting activation of RNF14. RNF25 catalyzes ubiquitination of other ribosomal proteins on stalled ribosomes, such as RPL0, RPL1, RPL12, RPS13 and …

**Summary**, from NCBI Gene [64320](https://www.ncbi.nlm.nih.gov/gene/64320):

> The protein encoded by this gene contains a RING finger motif. The mouse counterpart of this protein has been shown to interact with Rela, the p65 subunit of NF-kappaB (NFKB), and modulate NFKB-mediated transcription activity. The mouse protein also binds ubiquitin-conjugating enzymes (E2s) and is a substrate for E2-dependent ubiquitination. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14662) · Entrez [64320](https://www.ncbi.nlm.nih.gov/gene/64320) · UniProt [Q96BH1](https://www.uniprot.org/uniprotkb/Q96BH1) · Ensembl [ENSG00000163481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163481)

## Data

Gene col 8698: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8698); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8698, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8698]; `tensor/DDL_lfc|DDL_z.npy` [8698]; `embed/gene_vectors.npy` [8698]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8698 or target_col == 8698). Every well: [[RNF25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
