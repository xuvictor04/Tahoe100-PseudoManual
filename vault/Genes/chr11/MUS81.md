---
symbol: "MUS81"
type: "gene"
col: 10287
ensembl_id: "ENSG00000172732"
name: "MUS81 structure-specific endonuclease subunit"
location: "11q13"
module: 2
arm: "+"
pooled_cpm: 14.98
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MUS81

*MUS81 structure-specific endonuclease subunit* — 11q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +5.5, q 2e-05, up in 12 of 27 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.99×, SW480 2.96×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.765× (z -5.2, q 9e-05, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT2]] (+0.67, fdr 1e-05), [[ZYX]] (+0.63, fdr 7e-06), [[ARFRP1]] (+0.55, fdr 4e-05); moves opposite to [[PERP]] (-0.43, fdr 1e-04), [[RORA-AS1]] (-0.43, fdr 7e-05), [[TXN]] (-0.42, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10287.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 4.99×, SW480 2.96×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.5 | 2e-05 | 12/27 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.3 | 0.004 | 19/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.2 | 0.005 | 14/33 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.40× | +3.3 | 0.13 | 15/44 (MIA PaCa-2, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.39× | +3.2 | 0.13 | 16/44 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.13 | 11/45 (NCI-H460, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -5.2 | 9e-05 | 24/47 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -5.0 | 2e-04 | 27/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -4.9 | 2e-04 | 22/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -4.5 | 8e-04 | 22/47 (SW48, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.5 | 8e-04 | 20/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -4.3 | 0.002 | 20/47 (NCI-H2347, Hs 766T, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -4.2 | 0.002 | 16/46 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.727×** | -4.2 | 0.002 | 19/45 (AN3 CA, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.003 | 19/46 (H4, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.753×** | -3.9 | 0.005 | 13/48 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.779×** | -3.5 | 0.028 | 17/47 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.774×** | -3.4 | 0.030 | 18/42 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.031 | 15/46 (BT-474, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.787×** | -3.3 | 0.036 | 15/47 (PANC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.736×** | -3.0 | 0.093 | 3/47 (SNU-423, C32, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0892× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -13.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.265× (z -8.6) ⚠ toxic |
| [[A549 (line)]] | wt | 13.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.116× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0409× (z -14.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.80 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -9.3) |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.193× (z -8.5) |
| [[SW480 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT2]] | +0.67 | +0.57 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[ZYX]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ARFRP1]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ZNF598]] | +0.54 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[CPSF1]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TUBGCP6]] | +0.54 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[KIFC2]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[E2F4]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[DGKQ]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[PGAP6]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[SRF]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[GBA2]] | +0.50 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PERP]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[RORA-AS1]] | -0.43 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[TXN]] | -0.42 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[STPG4]] | -0.40 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[MGST2]] | -0.40 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[TMPRSS3]] | -0.40 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.0, -25.1); signed map (-6.5, 31.6). **Vector** length 65.1, 10.4% of its response variance represented; |z| ≥ 3 in 735 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +1.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.0 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | -2.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Aliskiren (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MUS81 structure-specific endonuclease subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13 — chr11:65,857,126-65,867,653 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44872, SLX3 |
| Reactome | 8 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; Fanconi Anemia Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NY9](https://www.uniprot.org/uniprotkb/Q96NY9) (Structure-specific endonuclease subunit MUS81):

> Catalytic subunit of two functionally distinct, structure-specific, heterodimeric DNA endonucleases MUS81-EME1 and MUS81-EME2 that are involved in the maintenance of genome stability. Both endonucleases have essentially the same substrate specificity though MUS81-EME2 is more active than its MUS81-EME1 counterpart. Both cleave 3'-flaps and nicked Holliday junctions, and exhibit limited endonuclease activity with 5' flaps and nicked double-stranded DNAs. MUS81-EME2 which is active during the …

**Summary**, from NCBI Gene [80198](https://www.ncbi.nlm.nih.gov/gene/80198):

> This gene encodes a structure-specific endonuclease which belongs to the XPF/MUS81 endonuclease family and plays a critical role in the resolution of recombination intermediates during DNA repair after inter-strand cross-links, replication fork collapse, and DNA double-strand breaks. The encoded protein associates with one of two closely related essential meiotic endonuclease proteins (EME1 or EME2) to form a complex that processes DNA secondary structures. It contains an N-terminal DEAH …

**Accessions** — [HGNC:29814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29814) · Entrez [80198](https://www.ncbi.nlm.nih.gov/gene/80198) · UniProt [Q96NY9](https://www.uniprot.org/uniprotkb/Q96NY9) · Ensembl [ENSG00000172732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172732)

## Data

Gene col 10287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10287); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10287]; `tensor/DDL_lfc|DDL_z.npy` [10287]; `embed/gene_vectors.npy` [10287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10287 or target_col == 10287). Every well: [[MUS81 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUS81.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
