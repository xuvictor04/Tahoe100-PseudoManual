---
symbol: "SNHG12"
type: "gene"
col: 12508
ensembl_id: "ENSG00000197989"
name: "small nucleolar RNA host gene 12"
location: "1p35.3"
module: 20
arm: "-"
pooled_cpm: 30.53
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNHG12

*small nucleolar RNA host gene 12* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.48× (z +10.7, q 3e-24, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.86, fdr 7e-06), [[SNHG8]] (+0.85, fdr 7e-06), [[SNHG7]] (+0.84, fdr 7e-06); moves opposite to [[BANF1]] (-0.68, fdr 7e-06), [[TGOLN2]] (-0.65, fdr 7e-06), [[NUP155]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.48×** | +10.7 | 3e-24 | 44/47 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.41×** | +7.5 | 2e-11 | 42/47 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +6.4 | 3e-08 | 37/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.93×** | +6.3 | 4e-08 | 39/44 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +5.6 | 2e-06 | 37/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.41×** | +5.2 | 2e-05 | 37/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.28×** | +5.0 | 4e-05 | 42/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.24×** | +4.9 | 6e-05 | 38/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.25×** | +4.9 | 6e-05 | 27/41 (SK-MEL-2, NCI-H460, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.12×** | +4.6 | 3e-04 | 39/47 (HT-29, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.01×** | +4.3 | 0.001 | 33/48 (KATO III, LS 180, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.46×** | +4.0 | 0.004 | 33/40 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.004 | 32/48 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.92×** | +3.7 | 0.008 | 33/48 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +3.6 | 0.013 | 35/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.043 | 29/48 (SW480, KATO III, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.62×** | +3.1 | 0.063 | 29/45 (SK-MEL-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.0 | 0.084 | 30/47 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.601× | -3.1 | 0.51 | 30/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.378× | -3.1 | 0.51 | 25/45 (SNU-423, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +10.4) | — |
| [[KATO III (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +8.5) | — |
| [[LoVo (line)]] | wt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.25× (z +8.5) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +11.0) | — |
| [[SW480 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +9.8) | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 76.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG8]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG7]] | +0.84 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG32]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | same gene group |
| [[ZFAS1]] | +0.82 | +0.77 / +0.84 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.75 | +0.70 / +0.81 | both halves | 7e-06 | same gene group |
| [[TAF1D]] | +0.75 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[EIF1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[GAS5]] | +0.71 | +0.61 / +0.77 | both halves | 7e-06 | same gene group |
| [[SAT2]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ATF4]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.68 | +0.58 / +0.69 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXW5]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BANF1]] | -0.68 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[TGOLN2]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[NUP155]] | -0.65 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[VMA21]] | -0.64 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[PRKDC]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[DR1]] | -0.64 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[TMEM19]] | -0.63 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.63 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[SRP9]] | -0.63 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.63 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[XRCC6]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.62 | -0.63 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.8, -28.9); signed map (-15.2, -2.2). **Vector** length 104, 35.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 12 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p35.3 — chr1:28,578,538-28,583,132 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PNAS-123, LINC00100, ASLNC04080; previously C1orf79 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

UniProt [Q9BXW3](https://www.uniprot.org/uniprotkb/Q9BXW3) carries no function annotation.

**Summary**, from NCBI Gene [85028](https://www.ncbi.nlm.nih.gov/gene/85028):

> This gene produces a long RNA that is overexpressed in tumor cells. This RNA may promote tumorigenesis by acting as a sponge for microRNAs. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:30062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30062) · Entrez [85028](https://www.ncbi.nlm.nih.gov/gene/85028) · UniProt [Q9BXW3](https://www.uniprot.org/uniprotkb/Q9BXW3) · Ensembl [ENSG00000197989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197989)

## Data

Gene col 12508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12508); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12508]; `tensor/DDL_lfc|DDL_z.npy` [12508]; `embed/gene_vectors.npy` [12508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12508 or target_col == 12508). Every well: [[SNHG12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
