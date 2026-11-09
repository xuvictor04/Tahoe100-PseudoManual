---
symbol: "MRPL4"
type: "gene"
col: 2589
ensembl_id: "ENSG00000105364"
name: "mitochondrial ribosomal protein L4"
location: "19p13.2"
module: 33
arm: "+"
pooled_cpm: 11.02
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MRPL4

*mitochondrial ribosomal protein L4* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +11.7, q 8e-29, up in 32 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.57× (z +4.9, q 5e-05, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.761× (z -4.2, q 0.012, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.242×); [[Saquinavir (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0664×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C20orf27]] (+0.74, fdr 7e-06), [[DCTPP1]] (+0.74, fdr 7e-06), [[PHB1]] (+0.73, fdr 7e-06); moves opposite to [[SMIM14]] (-0.64, fdr 1e-05), [[PPP1R12A-AS2]] (-0.62, fdr 1e-04), [[LINC01004]] (-0.62, fdr 8e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.92×** | +11.7 | 8e-29 | 32/35 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.49×** | +9.6 | 3e-19 | 14/17 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.39×** | +9.5 | 4e-19 | 42/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.51×** | +9.3 | 3e-18 | 25/28 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.26×** | +8.9 | 7e-17 | 38/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.89×** | +6.9 | 4e-10 | 37/47 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +6.7 | 1e-09 | 26/40 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.73×** | +5.8 | 6e-07 | 24/41 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.9 | 5e-05 | 25/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.45×** | +4.1 | 0.003 | 20/41 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.003 | 14/45 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.8 | 0.006 | 7/19 (NCI-H2347, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.007 | 15/47 (HOP62, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.010 | 8/45 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.40×** | +3.6 | 0.011 | 14/46 (SW480, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.013 | 18/46 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.067 | 12/43 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 0.242×); [[Saquinavir (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0664×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.012 | 18/46 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.727× | -3.5 | 0.13 | 13/47 (LOX-IMVI, C32, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (drug)]] 5 µM |  | 0.816× | -3.2 | 0.29 | 10/48 (NCI-H661, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 6.43 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0664× (z -10.4) |
| [[SW48 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf27]] | +0.74 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DCTPP1]] | +0.74 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PHB1]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[NLE1]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RITA1]] | +0.70 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.70 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PTGES2]] | +0.69 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NOL10]] | +0.68 | +0.66 / +0.58 | both halves | 7e-06 | STRING 530 |
| [[RPUSD1]] | +0.68 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.68 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[MCAT]] | +0.68 | +0.57 / +0.62 | both halves | 1e-05 | STRING 663 |
| [[DHODH]] | +0.67 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.62 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[USP34-DT]] | -0.61 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[KMT2E-AS1]] | -0.59 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[KRBOX5]] | -0.59 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[TSGA10]] | -0.59 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[LINC00910]] | -0.58 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | -0.58 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[CABYR]] | -0.57 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.7, -41.6); signed map (-10.5, -52.0). **Vector** length 58.0, 9.68% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.52 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.7 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.6 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.5 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.5 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,251,901-10,260,055 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-28, uL4m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYD3](https://www.uniprot.org/uniprotkb/Q9BYD3) carries no function annotation.

**Summary**, from NCBI Gene [51073](https://www.ncbi.nlm.nih.gov/gene/51073):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14276) · Entrez [51073](https://www.ncbi.nlm.nih.gov/gene/51073) · UniProt [Q9BYD3](https://www.uniprot.org/uniprotkb/Q9BYD3) · Ensembl [ENSG00000105364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105364)

## Data

Gene col 2589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2589); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2589]; `tensor/DDL_lfc|DDL_z.npy` [2589]; `embed/gene_vectors.npy` [2589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2589 or target_col == 2589). Every well: [[MRPL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
