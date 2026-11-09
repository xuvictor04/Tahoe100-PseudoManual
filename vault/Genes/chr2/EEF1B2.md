---
symbol: "EEF1B2"
type: "gene"
col: 3604
ensembl_id: "ENSG00000114942"
name: "eukaryotic translation elongation factor 1 beta 2"
location: "2q33.3"
module: 43
arm: "+"
pooled_cpm: 114.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EEF1B2

*eukaryotic translation elongation factor 1 beta 2* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +10.9, q 7e-25, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +4.4, q 0.001, up in 35 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS4X]] (+0.76, fdr 7e-06), [[RPL30]] (+0.73, fdr 7e-06, ⚠ RPL30 in the vector space only through flagged drug-doses), [[RPL14]] (+0.73, fdr 7e-06), [[RPL27A]] (+0.72, fdr 7e-06); moves opposite to [[MRPL28]] (-0.55, fdr 3e-05), [[ACP2]] (-0.50, fdr 3e-05), [[MRPL35]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3604.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +10.9 | 7e-25 | 48/49 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +10.4 | 9e-23 | 44/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +7.9 | 7e-13 | 45/45 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.0 | 3e-07 | 44/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.85×** | +5.6 | 2e-06 | 45/48 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.001 | 35/49 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 39/48 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.0 | 0.005 | 39/47 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.43×** | +3.3 | 0.069 | 33/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.081 | 27/48 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.41× | +3.0 | 0.12 | 26/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 69.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 158 | 3 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.87× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 112 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +10.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 109 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 59.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 62.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 105 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 94.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 146 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 54.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 88.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 217 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 96.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 77.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 57.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +8.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 92.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 79.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 130 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 90.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 214 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS4X]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 927 |
| [[RPL30]] ⚠ | +0.73 | +0.62 / +0.77 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 970; ⚠ in the vector space only through flagged drug-doses |
| [[RPL14]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 963 |
| [[RPL27A]] | +0.72 | +0.58 / +0.80 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 964 |
| [[RPL10A]] ⚠ | +0.72 | +0.71 / +0.74 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 963; ⚠ in the vector space only through flagged drug-doses |
| [[RPL7]] | +0.72 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 932 |
| [[RPLP0]] | +0.71 | +0.59 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 988 |
| [[RPL22]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 838 |
| [[RPL5]] | +0.69 | +0.70 / +0.70 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 973 |
| [[RPS20]] | +0.69 | +0.58 / +0.74 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 982 |
| [[RPL24]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 980 |
| [[RPL21]] ⚠ | +0.68 | +0.58 / +0.69 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 989; ⚠ in the vector space only through flagged drug-doses |
| [[BTF3]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | STRING 637 |
| [[RPL13A]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 930 |
| [[RACK1]] | +0.68 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 993 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL28]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ACP2]] | -0.50 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MRPL35]] | -0.50 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[RAB8A]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.9, -30.4); signed map (-60.5, -6.8). **Vector** length 65.5, 24.8% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Peptide chain elongation* (reactome, mean cos +0.61 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.61 to 53); *Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC)* (reactome, mean cos +0.61 to 52).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | -1.9 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.0 | -1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | -2.8 | +5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -2.6 | +3.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.2 |
|  | [[Flutamide (drug)]] 5 µM |  | -1.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:206,159,585-206,162,928 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Eukaryotic Translation Elongation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P24534](https://www.uniprot.org/uniprotkb/P24534) (Elongation factor 1-beta):

> Catalytic subunit of the guanine nucleotide exchange factor (GEF) (eEF1B subcomplex) of the eukaryotic elongation factor 1 complex (eEF1) (By similarity). Stimulates the exchange of GDP for GTP on elongation factor 1A (eEF1A), probably by displacing GDP from the nucleotide binding pocket in eEF1A (By similarity).

**Summary**, from NCBI Gene [1933](https://www.ncbi.nlm.nih.gov/gene/1933):

> This gene encodes a translation elongation factor. The protein is a guanine nucleotide exchange factor involved in the transfer of aminoacylated tRNAs to the ribosome. Alternative splicing results in three transcript variants which differ only in the 5' UTR. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3208) · Entrez [1933](https://www.ncbi.nlm.nih.gov/gene/1933) · UniProt [P24534](https://www.uniprot.org/uniprotkb/P24534) · Ensembl [ENSG00000114942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114942)

## Data

Gene col 3604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3604); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3604]; `tensor/DDL_lfc|DDL_z.npy` [3604]; `embed/gene_vectors.npy` [3604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3604 or target_col == 3604). Every well: [[EEF1B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
