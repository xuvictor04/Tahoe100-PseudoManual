---
symbol: "UNC50"
type: "gene"
col: 3676
ensembl_id: "ENSG00000115446"
name: "unc-50 inner nuclear membrane RNA binding protein"
location: "2q11.2"
module: 15
arm: "+"
pooled_cpm: 20.79
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# UNC50

*unc-50 inner nuclear membrane RNA binding protein* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.29× (z +6.5, q 4e-08, up in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.26× (z +4.1, q 0.007, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.473× (z -13.4, q 4e-38, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRYD4]] (+0.66, fdr 2e-05), [[TMEM147-AS1]] (+0.65, fdr 1e-05), [[MTHFSD]] (+0.64, fdr 3e-05); moves opposite to [[RNF24]] (-0.66, fdr 1e-05), [[CARHSP1]] (-0.64, fdr 3e-05), [[RHPN2]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.29×** | +6.5 | 4e-08 | 20/48 (SNU-1, HS-578T, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +6.3 | 7e-08 | 19/37 (SNU-423, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.6 | 3e-06 | 24/44 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.007 | 15/47 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.050 | 17/44 (J82, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.20 | 16/47 (LoVo, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -13.4 | 4e-38 | 43/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -12.8 | 3e-35 | 42/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.516×** | -11.8 | 4e-30 | 42/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.9 | 3e-13 | 35/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.648×** | -7.8 | 9e-13 | 32/48 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.653×** | -6.9 | 4e-10 | 25/47 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.636×** | -4.2 | 0.002 | 17/40 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.658×** | -3.9 | 0.006 | 17/48 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.813×** | -3.7 | 0.013 | 12/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.028 | 10/48 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.822×** | -3.2 | 0.073 | 10/48 (SNU-1, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.838× | -3.2 | 0.075 | 16/47 (SW48, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.886× | -3.1 | 0.093 | 16/47 (RKO, A549, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.845× | -3.0 | 0.10 | 16/47 (BT-474, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -10.6) |
| [[SW480 (line)]] | alt | 24.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.0) |
| [[A549 (line)]] | wt | 18.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 22.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 21.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -9.6) |
| [[RKO (line)]] | wt | 24.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0986× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0860× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRYD4]] | +0.66 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.64 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RNASEH1]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[LAMTOR1]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.63 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | +0.63 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ZNF514]] | +0.61 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[GTF3C2-AS2]] | +0.60 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[PPP1R3F]] | +0.59 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[DVL3]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PSKH1]] | +0.59 | +0.53 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF24]] | -0.66 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.64 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RHPN2]] | -0.61 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[FAM13B]] | -0.57 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[CFD]] | -0.57 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ARL3]] | -0.56 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[MYO1E]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[LGALS1]] | -0.55 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[JPT1]] | -0.54 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[ABCB9]] | -0.54 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[RAB11FIP1]] | -0.54 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[PAFAH1B3]] | -0.54 | -0.36 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.6, 9.1); signed map (7.0, -34.4). **Vector** length 82.5, 15.5% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.4 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -13.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | unc-50 inner nuclear membrane RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:98,608,579-98,618,515 (+) |
| Ensembl biotype | protein_coding |
| Also known as | URP, UNCL, GMH1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53HI1](https://www.uniprot.org/uniprotkb/Q53HI1) (Protein unc-50 homolog):

> Involved in the cell surface expression of neuronal nicotinic receptors (By similarity). Binds RNA (By similarity).

**Summary**, from NCBI Gene [25972](https://www.ncbi.nlm.nih.gov/gene/25972):

> Predicted to enable RNA binding activity. Predicted to be involved in protein localization to cell surface. Predicted to be located in nuclear inner membrane. Predicted to be active in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16046) · Entrez [25972](https://www.ncbi.nlm.nih.gov/gene/25972) · UniProt [Q53HI1](https://www.uniprot.org/uniprotkb/Q53HI1) · Ensembl [ENSG00000115446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115446)

## Data

Gene col 3676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3676); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3676]; `tensor/DDL_lfc|DDL_z.npy` [3676]; `embed/gene_vectors.npy` [3676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3676 or target_col == 3676). Every well: [[UNC50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
