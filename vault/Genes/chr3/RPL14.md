---
symbol: "RPL14"
type: "gene"
col: 12056
ensembl_id: "ENSG00000188846"
name: "ribosomal protein L14"
location: "3p22.1"
module: 43
arm: "+"
pooled_cpm: 112.84
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL14

*ribosomal protein L14* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.55× (z +13.9, q 7e-41, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.53× (z +4.7, q 3e-04, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1G]] (+0.84, fdr 7e-06), [[RPS7]] (+0.80, fdr 7e-06), [[RPS3A]] (+0.78, fdr 7e-06); moves opposite to [[TUBB4B]] (-0.56, fdr 1e-05), [[SLC35A4]] (-0.53, fdr 1e-04), [[CEP295]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +13.9 | 7e-41 | 48/49 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +12.5 | 1e-33 | 44/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +9.5 | 3e-19 | 43/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.25×** | +8.4 | 5e-15 | 32/50 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.5 | 6e-06 | 41/47 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 3e-04 | 39/48 (SW1417, HT-29, …) | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 30/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.004 | 29/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.41×** | +3.8 | 0.011 | 37/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +3.7 | 0.013 | 35/49 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.013 | 34/48 (RPMI-7951, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.6 | 0.013 | 31/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.041 | 26/48 (BT-474, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.712× | -3.7 | 0.12 | 41/49 (SW480, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 92.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +13.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +15.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +13.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 140 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 151 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +15.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 78.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 96.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +13.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 86.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 96.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 89.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 59.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 89.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 78.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 80.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 60.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.99× (z +13.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 73.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 186 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[RKO (line)]] | wt | 198 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 94.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 75.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1G]] | +0.84 | +0.78 / +0.83 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 939 |
| [[RPS7]] | +0.80 | +0.75 / +0.75 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3A]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS2]] | +0.77 | +0.71 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPL3]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL29]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS20]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL39]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL22]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPS18]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB4B]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.53 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[CEP295]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[THOP1]] | -0.52 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[THSD8]] ⚠ | -0.51 | -0.39 / -0.56 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ERVK3-1]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.7, -30.5); signed map (-60.7, -7.2). **Vector** length 82.7, 27.1% of its response variance represented; |z| ≥ 3 in 613 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.57 to 19); *Translation initiation complex formation* (reactome, mean cos +0.57 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.57 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | -0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.3 | -1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.0 | +1.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.9 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:40,457,292-40,468,587 (+) |
| Ensembl biotype | protein_coding |
| Also known as | L14, hRL14, RL14, CTG-B33, eL14 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P50914](https://www.uniprot.org/uniprotkb/P50914) (Large ribosomal subunit protein eL14):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [9045](https://www.ncbi.nlm.nih.gov/gene/9045):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L14E family of ribosomal proteins. It contains a basic region-leucine zipper (bZIP)-like domain. The protein is located in the cytoplasm. This gene contains a trinucleotide …

**Accessions** — [HGNC:10305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10305) · Entrez [9045](https://www.ncbi.nlm.nih.gov/gene/9045) · UniProt [P50914](https://www.uniprot.org/uniprotkb/P50914) · Ensembl [ENSG00000188846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188846)

## Data

Gene col 12056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12056); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12056]; `tensor/DDL_lfc|DDL_z.npy` [12056]; `embed/gene_vectors.npy` [12056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12056 or target_col == 12056). Every well: [[RPL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
