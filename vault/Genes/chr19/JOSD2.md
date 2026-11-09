---
symbol: "JOSD2"
type: "gene"
col: 8448
ensembl_id: "ENSG00000161677"
name: "Josephin domain containing 2"
location: "19q13.33"
module: 24
arm: "+"
pooled_cpm: 6.58
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# JOSD2

*Josephin domain containing 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +5.2, q 1e-04, up in 19 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.46× (z +3.5, q 0.075, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -11.7, q 5e-29, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP21]] (+0.74, fdr 1e-05), [[CHCHD5]] (+0.70, fdr 1e-05), [[BLVRB]] (+0.68, fdr 9e-06); moves opposite to [[CBX5]] (-0.62, fdr 4e-05), [[SRSF1]] (-0.61, fdr 1e-05), [[SYNCRIP]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +5.2 | 1e-04 | 19/28 (SW480, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.6 | 0.075 | 18/35 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +3.5 | 0.075 | 4/16 (MIA PaCa-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.075 | 21/45 (CFPAC-1, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.61× | +3.1 | 0.22 | 13/33 (A-427, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8448.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.283×** | -11.7 | 5e-29 | 38/40 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.315×** | -7.6 | 9e-12 | 38/47 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.352×** | -6.8 | 1e-09 | 36/44 (H4, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -5.9 | 5e-07 | 32/38 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.244×** | -4.8 | 1e-04 | 27/42 (SW480, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.486×** | -4.7 | 2e-04 | 28/47 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -4.7 | 2e-04 | 30/44 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.510×** | -4.4 | 7e-04 | 27/43 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -4.4 | 7e-04 | 28/40 (C-33 A, SW1417, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.529×** | -4.2 | 0.002 | 26/44 (C-33 A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.320×** | -3.9 | 0.005 | 24/39 (PANC-1, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.574×** | -3.7 | 0.012 | 19/45 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -3.6 | 0.014 | 20/44 (KATO III, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.585×** | -3.5 | 0.017 | 21/44 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -3.1 | 0.075 | 14/45 (CHP-212, AN3 CA, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.611×** | -3.0 | 0.094 | 13/44 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -13.9) |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 7.54 | 0 | 2 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0396× (z -11.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0721× (z -9.7) |
| [[HOP62 (line)]] | alt | 6.59 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0354× (z -13.7) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -11.5) |
| [[A498 (line)]] | wt | 9.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.8) |
| [[A549 (line)]] | wt | 9.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -8.5) |
| [[HT-29 (line)]] | alt | 7.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 5.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 9.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 7.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0771× (z -13.0) |
| [[A-427 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 10 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP21]] | +0.74 | +0.56 / +0.80 | both halves | 1e-05 |  |
| [[CHCHD5]] | +0.70 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.68 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[IFI27L2]] | +0.67 | +0.39 / +0.76 | both halves | 6e-05 |  |
| [[NOL7]] ⚠ | +0.67 | +0.41 / +0.72 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TRAPPC5]] | +0.65 | +0.28 / +0.77 | both halves | 3e-04 |  |
| [[POLR2I]] | +0.65 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[RNF181]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.64 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SSNA1]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PEX16]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ARL8A]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | -0.62 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[SRSF1]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SYNCRIP]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[TMPO]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[SRP9]] | -0.59 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[TMEM123]] | -0.58 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[CAPRIN1]] | -0.57 | -0.30 / -0.67 | both halves | 2e-04 |  |
| [[SEPTIN11]] | -0.56 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[LMNB2]] | -0.56 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[ERLIN2]] | -0.56 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.55 | -0.26 / -0.66 | both halves | 3e-04 |  |
| [[HNRNPUL1]] | -0.55 | -0.21 / -0.60 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.2, -15.6); signed map (-18.1, -4.6). **Vector** length 60.2, 11.7% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -5.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -7.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Josephin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,505,998-50,511,220 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SBBI54 |
| Gene groups (HGNC) | JOSD family MJD deubiquinating enzymes |
| Reactome | 2 pathways, smallest: Josephin domain DUBs; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAC2](https://www.uniprot.org/uniprotkb/Q8TAC2) (Josephin-2):

> Cleaves 'Lys-63'-linked poly-ubiquitin chains, and with lesser efficiency 'Lys-48'-linked poly-ubiquitin chains (in vitro). May act as a deubiquitinating enzyme.

**Summary**, from NCBI Gene [126119](https://www.ncbi.nlm.nih.gov/gene/126119):

> This gene encodes a protein containing a Josephin domain. Josephin domain-containing proteins are deubiquitinating enzymes which catalyze the hydrolysis of the bond between the C-terminal glycine of the ubiquitin peptide and protein substrates. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:28853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28853) · Entrez [126119](https://www.ncbi.nlm.nih.gov/gene/126119) · UniProt [Q8TAC2](https://www.uniprot.org/uniprotkb/Q8TAC2) · Ensembl [ENSG00000161677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161677)

## Data

Gene col 8448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8448); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8448]; `tensor/DDL_lfc|DDL_z.npy` [8448]; `embed/gene_vectors.npy` [8448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8448 or target_col == 8448). Every well: [[JOSD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JOSD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
