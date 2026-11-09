---
symbol: "TINF2"
type: "gene"
col: 1697
ensembl_id: "ENSG00000092330"
name: "TERF1 interacting nuclear factor 2"
location: "14q12"
module: 2
arm: "+"
pooled_cpm: 10.33
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TINF2

*TERF1 interacting nuclear factor 2* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +4.6, q 0.002, up in 16 of 44 measured lines) ⚠ cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.22× (z +4.0, q 0.016, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.506× (z -9.6, q 3e-19, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.587× (z -7.5, q 1e-11, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK7]] (+0.67, fdr 7e-06), [[RIC8A]] (+0.64, fdr 1e-05), [[ABCD1]] (+0.62, fdr 1e-05); moves opposite to [[LUC7L3]] (-0.62, fdr 1e-05), [[PABPN1]] (-0.61, fdr 1e-05), [[PNISR]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +4.6 | 0.002 | 16/44 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.016 | 18/48 (BT-474, Hs 766T, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.9 | 0.016 | 2/48 (NCI-H1573, NCI-H23) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.9 | 0.016 | 11/40 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +3.8 | 0.017 | 12/47 (NCI-H2347, BT-474, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.017 | 12/46 (LS 180, HT-29, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +3.5 | 0.042 | 18/47 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.3 | 0.077 | 6/20 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.23× | +3.0 | 0.16 | 10/47 (SW480, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -9.6 | 3e-19 | 30/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.674×** | -7.9 | 9e-13 | 29/45 (HS-578T, RPMI-7951, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -7.5 | 1e-11 | 27/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -6.9 | 5e-10 | 29/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -6.9 | 7e-10 | 28/47 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.611×** | -3.6 | 0.025 | 9/19 (NCI-H1573, A549, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.6 | 0.026 | 16/37 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.629×** | -3.4 | 0.042 | 8/40 (RPMI-7951, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.785×** | -3.4 | 0.042 | 15/43 (J82, AsPC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.065 | 13/43 (H4, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.655×** | -3.1 | 0.092 | 9/44 (NCI-H460, HepG2/C3A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.794×** | -3.1 | 0.099 | 11/47 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.805×** | -3.1 | 0.099 | 13/46 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.73 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0860× (z -9.4) |
| [[HOP62 (line)]] | alt | 8.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.84 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0817× (z -9.2) |
| [[LoVo (line)]] | wt | 9.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0682× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -9.7) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 15.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.236× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0948× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK7]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[RIC8A]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ABCD1]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CHMP7]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[IPO13]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[RAB8A]] | +0.57 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[MTFR1L]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[CD68]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CORO1B]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ACD]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 | same gene group; pathway: Base Excision Repair; STRING 999 |
| [[KCTD5]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUC7L3]] | -0.62 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[PABPN1]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PNISR]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PRPF4B]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[COX5A]] ⚠ | -0.49 | -0.61 / -0.32 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[VAMP2]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[HOXB5]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[LCORL]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ATP5MC2]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.327). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-29.8, -12.0); signed map (-25.4, 3.2). **Vector** length 70.6, 11.2% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.8 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.7 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TERF1 interacting nuclear factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,238,286-24,242,663 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIN2 |
| Gene groups (HGNC) | Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSI4](https://www.uniprot.org/uniprotkb/Q9BSI4) (TERF1-interacting nuclear factor 2):

> Component of the shelterin complex (telosome) that is involved in the regulation of telomere length and protection. Shelterin associates with arrays of double-stranded TTAGGG repeats added by telomerase and protects chromosome ends; without its protective activity, telomeres are no longer hidden from the DNA damage surveillance and chromosome ends are inappropriately processed by DNA repair pathways. Plays a role in shelterin complex assembly. Isoform 1 may have additional role in tethering …

**Summary**, from NCBI Gene [26277](https://www.ncbi.nlm.nih.gov/gene/26277):

> This gene encodes one of the proteins of the shelterin, or telosome, complex which protects telomeres by allowing the cell to distinguish between telomeres and regions of DNA damage. The protein encoded by this gene is a critical part of shelterin; it interacts with the three DNA-binding proteins of the shelterin complex, and it is important for assembly of the complex. Mutations in this gene cause dyskeratosis congenita (DKC), an inherited bone marrow failure syndrome. [provided by RefSeq, Mar …

**Accessions** — [HGNC:11824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11824) · Entrez [26277](https://www.ncbi.nlm.nih.gov/gene/26277) · UniProt [Q9BSI4](https://www.uniprot.org/uniprotkb/Q9BSI4) · Ensembl [ENSG00000092330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092330)

## Data

Gene col 1697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1697); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1697]; `tensor/DDL_lfc|DDL_z.npy` [1697]; `embed/gene_vectors.npy` [1697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1697 or target_col == 1697). Every well: [[TINF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TINF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
