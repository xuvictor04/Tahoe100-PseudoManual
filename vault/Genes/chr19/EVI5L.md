---
symbol: "EVI5L"
type: "gene"
col: 6624
ensembl_id: "ENSG00000142459"
name: "ecotropic viral integration site 5 like"
location: "19p13.2"
module: 52
arm: "+"
pooled_cpm: 12.09
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# EVI5L

*ecotropic viral integration site 5 like* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.01× (z +23.3, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.731× (z -7.5, q 5e-11, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TECPR1]] (+0.70, fdr 1e-05), [[TSC2]] (+0.63, fdr 3e-05), [[TMEM184B]] (+0.62, fdr 3e-05); moves opposite to [[PUM1]] (-0.57, fdr 1e-04), [[PATL2]] (-0.55, fdr 3e-04), [[ZNF300]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.01×** | +23.3 | 0e+00 | 46/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.90×** | +22.8 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.86×** | +22.6 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +12.8 | 2e-35 | 43/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.08×** | +12.3 | 1e-32 | 36/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +9.1 | 6e-18 | 38/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +8.3 | 6e-15 | 14/24 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.9 | 4e-10 | 15/35 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.21×** | +4.4 | 6e-04 | 18/45 (A498, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 12/46 (SK-MEL-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.26×** | +3.7 | 0.010 | 13/40 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.011 | 7/42 (LoVo, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.020 | 5/47 (RKO, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.24×** | +3.4 | 0.028 | 8/30 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +3.4 | 0.028 | 11/45 (A498, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.079 | 10/47 (hTERT-HPNE, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.731×** | -7.5 | 5e-11 | 27/48 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.698×** | -6.1 | 4e-07 | 20/47 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -4.9 | 2e-04 | 10/47 (RKO, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -4.4 | 0.001 | 18/39 (SHP-77, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.009 | 13/46 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.655×** | -3.7 | 0.019 | 10/45 (HEC-1-A, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.061 | 9/48 (H4, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.823× | -3.2 | 0.11 | 9/47 (A498, HepG2/C3A, …) | top dose only |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.16 | 3/47 (A-172, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.15× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +12.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 7.24 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.58× (z +11.2) | — |
| [[SW480 (line)]] | alt | 10.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +11.6) | — |
| [[A-172 (line)]] | wt | 17.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +9.0) | — |
| [[A498 (line)]] | wt | 8.10 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.53× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 10.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.88× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 8.92 | 2 | 0 | [[Belinostat (drug)]] 5 µM 5.81× (z +8.6) | — |
| [[A549 (line)]] | wt | 4.50 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0647× (z -9.4) |
| [[BT-474 (line)]] | alt | 9.13 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0898× (z -9.1) |
| [[HCT15 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 9.02 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0865× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.311× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.259× (z -9.2) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.1000× (z -11.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | +0.70 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TSC2]] | +0.63 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TMEM184B]] | +0.62 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[MIGA2]] | +0.61 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[AP2A1]] | +0.61 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[MAP3K9]] | +0.59 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SLC25A16]] | +0.59 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[WIPI1]] | +0.59 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[OSTF1]] | +0.57 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[SNTA1]] | +0.57 | +0.39 / +0.30 | both halves | 2e-04 |  |
| [[PSMD9]] | +0.57 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[TMED9]] | +0.57 | +0.44 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM1]] | -0.57 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PATL2]] | -0.55 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[ZNF300]] | -0.55 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[NCR3LG1]] | -0.55 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[ATF7IP]] | -0.55 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ANKRD18B]] | -0.54 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[LINC02605]] | -0.54 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[CACHD1]] | -0.53 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[ZNF610]] | -0.53 | -0.26 / -0.30 | both halves | 3e-04 |  |
| [[RNLS]] | -0.52 | -0.21 / -0.34 | both halves | 7e-04 |  |
| [[RASEF]] | -0.52 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[EIF4G2]] | -0.51 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.0, 0.8); signed map (-35.5, -0.5). **Vector** length 79.2, 14.9% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.2 | +22.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +22.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +23.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.4 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -7.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.3 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | +0.1 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -3.2 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ecotropic viral integration site 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,830,218-7,864,976 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TBC1 domain family members; EVI5 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CN4](https://www.uniprot.org/uniprotkb/Q96CN4) (EVI5-like protein):

> Functions as a GTPase-activating protein (GAP) with a broad specificity.

**Summary**, from NCBI Gene [115704](https://www.ncbi.nlm.nih.gov/gene/115704):

> Enables GTPase activator activity and small GTPase binding activity. Involved in negative regulation of cilium assembly and positive regulation of GTPase activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30464) · Entrez [115704](https://www.ncbi.nlm.nih.gov/gene/115704) · UniProt [Q96CN4](https://www.uniprot.org/uniprotkb/Q96CN4) · Ensembl [ENSG00000142459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142459)

## Data

Gene col 6624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6624); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6624]; `tensor/DDL_lfc|DDL_z.npy` [6624]; `embed/gene_vectors.npy` [6624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6624 or target_col == 6624). Every well: [[EVI5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVI5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
