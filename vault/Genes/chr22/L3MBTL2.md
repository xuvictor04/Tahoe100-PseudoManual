---
symbol: "L3MBTL2"
type: "gene"
col: 1948
ensembl_id: "ENSG00000100395"
name: "L3MBTL histone methyl-lysine binding protein 2"
location: "22q13.2"
module: 7
arm: "+"
pooled_cpm: 9.99
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# L3MBTL2

*L3MBTL histone methyl-lysine binding protein 2* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.86× (z +10.4, q 1e-22, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.683× (z -9.1, q 3e-17, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF5A]] (+0.68, fdr 7e-06), [[FLAD1]] (+0.66, fdr 7e-06), [[SETD1A]] (+0.65, fdr 7e-06); moves opposite to [[NPTN]] (-0.60, fdr 2e-05), [[RYBP]] (-0.58, fdr 1e-05), [[PERP]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +10.4 | 1e-22 | 36/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +10.0 | 4e-21 | 35/45 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +8.0 | 2e-13 | 25/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 4e-12 | 26/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +7.6 | 4e-12 | 29/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.31×** | +7.4 | 1e-11 | 24/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +6.8 | 9e-10 | 21/43 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.9 | 2e-07 | 17/46 (COLO 205, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.8 | 4e-07 | 15/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.7 | 5e-07 | 21/45 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 1e-05 | 15/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 3e-05 | 17/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.9 | 5e-05 | 11/47 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +4.3 | 8e-04 | 5/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.003 | 6/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.683×** | -9.1 | 3e-17 | 31/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.622×** | -8.1 | 2e-13 | 21/35 (SK-MEL-2, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.2 | 9e-11 | 12/18 (HS-578T, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.683×** | -6.5 | 1e-08 | 24/45 (hTERT-HPNE, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.4 | 0.001 | 16/45 (HepG2/C3A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.835× | -4.3 | 0.001 | 17/48 (LoVo, LS 180, …) | rises with dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.837× | -3.0 | 0.20 | 4/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 11.6 | 0 | 2 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.100× (z -9.3) |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.07 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0789× (z -10.3) ⚠ cell-cycle shift, explains ~16% of this change |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0908× (z -10.1) |
| [[C32 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 10.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.199× (z -8.9) |
| [[LoVo (line)]] | wt | 8.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 7.49 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0697× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 8.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.17 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0874× (z -9.6) |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF5A]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SETD1A]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[WDR24]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[DDX51]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H18]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[TRMT2A]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DOLPP1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[LSG1]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[DHX30]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SDHAF2]] | +0.61 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[GPATCH3]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.60 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[RYBP]] | -0.58 | -0.55 / -0.61 | both halves | 1e-05 | pathway: Transcriptional Regulation by E2F6; STRING 978 |
| [[PERP]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TMSB4X]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SDCBP]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[EPB41L2]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ABI1]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.52 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[EPB41L5]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.524). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.0, 1.8); signed map (-10.3, -27.1). **Vector** length 64.4, 9.21% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +6.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | L3MBTL histone methyl-lysine binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,205,282-41,231,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H-l(3)mbt-l, DKFZP761I141, dJ756G23.3 |
| Gene groups (HGNC) | MBT domain containing |
| Reactome | 4 pathways, smallest: Transcriptional Regulation by E2F6; SUMOylation of chromatin organization proteins; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969R5](https://www.uniprot.org/uniprotkb/Q969R5) (Lethal(3)malignant brain tumor-like protein 2):

> Putative Polycomb group (PcG) protein. PcG proteins maintain the transcriptionally repressive state of genes, probably via a modification of chromatin, rendering it heritably changed in its expressibility. Its association with a chromatin-remodeling complex suggests that it may contribute to prevent expression of genes that trigger the cell into mitosis. Binds to monomethylated and dimethylated 'Lys-20' on histone H4. Binds histone H3 peptides that are monomethylated or dimethylated on 'Lys-4', …

**Summary**, from NCBI Gene [83746](https://www.ncbi.nlm.nih.gov/gene/83746):

> Enables histone H4K20me1 reader activity; histone H4K20me2 reader activity; and histone binding activity. Predicted to be involved in negative regulation of DNA-templated transcription. Predicted to act upstream of or within several processes, including ectoderm development; stem cell differentiation; and stem cell proliferation. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18594) · Entrez [83746](https://www.ncbi.nlm.nih.gov/gene/83746) · UniProt [Q969R5](https://www.uniprot.org/uniprotkb/Q969R5) · Ensembl [ENSG00000100395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100395)

## Data

Gene col 1948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1948); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1948]; `tensor/DDL_lfc|DDL_z.npy` [1948]; `embed/gene_vectors.npy` [1948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1948 or target_col == 1948). Every well: [[L3MBTL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3MBTL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
