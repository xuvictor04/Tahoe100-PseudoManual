---
symbol: "ATP1A1-AS1"
type: "gene"
col: 12795
ensembl_id: "ENSG00000203865"
name: "ATP1A1 antisense RNA 1"
location: "1p13.1"
module: 10
arm: "+"
pooled_cpm: 10.77
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ATP1A1-AS1

*ATP1A1 antisense RNA 1* — 1p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.84× (z +8.4, q 2e-14, up in 15 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +7.1, q 2e-10, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.740× (z -4.4, q 0.003, down in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.0913×, NCI-H23 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Trifluridine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0399×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (A-172 0.0938×); [[Canagliflozin (drug)]] 5 µM in 1 line (C-33 A 0.0732×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB5D2]] (+0.69, fdr 1e-05), [[DPH6-DT]] (+0.69, fdr 2e-05), [[IDNK]] (+0.69, fdr 1e-05); moves opposite to [[TMEM184B]] (-0.56, fdr 4e-04), [[ZNRF1]] (-0.55, fdr 4e-04), [[TMEM104]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +8.4 | 2e-14 | 15/22 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.4 | 5e-11 | 27/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +7.1 | 2e-10 | 24/48 (LS 180, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.4 | 2e-08 | 29/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +5.8 | 6e-07 | 23/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +5.2 | 2e-05 | 15/32 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 1e-04 | 15/46 (C32, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **1.24×** | +4.4 | 9e-04 | 11/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.3 | 1e-03 | 18/46 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.1 | 0.002 | 14/40 (SNU-423, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 10/47 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.036 | 13/47 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.036 | 5/47 (RKO, A-427, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.042 | 10/46 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.061 | 6/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.061 | 6/47 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.064 | 4/47 (H4, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.081 | 12/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.100 | 9/43 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.0913×, NCI-H23 0.198×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Trifluridine (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0399×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (A-172 0.0938×); [[Canagliflozin (drug)]] 5 µM in 1 line (C-33 A 0.0732×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -4.4 | 0.003 | 19/44 (H4, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -4.4 | 0.003 | 19/47 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -4.3 | 0.003 | 4/48 (SHP-77, AN3 CA, …) | inconsistent across doses |  |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.799× | -3.3 | 0.15 | 8/48 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.51 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -8.9) |
| [[A-172 (line)]] | wt | 8.72 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0938× (z -11.1) |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0732× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 7.65 | 0 | 1 | — | [[Trifluridine (drug)]] 0.05 µM 0.0399× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[RKO (line)]] | wt | 8.37 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0989× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | +0.69 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[DPH6-DT]] | +0.69 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[IDNK]] | +0.69 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.68 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[FAM227B]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.66 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[HNRNPK-AS1]] | +0.66 | +0.44 / +0.54 | both halves | 3e-05 | same gene group |
| [[ENTPD3-AS1]] | +0.64 | +0.62 / +0.40 | both halves | 5e-05 | same gene group |
| [[ZRANB2-DT]] | +0.64 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[TAFA2]] | +0.64 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[EIF1B-AS1]] | +0.64 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[LINC01376]] | +0.63 | +0.69 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | -0.56 | -0.63 / -0.25 | both halves | 4e-04 |  |
| [[ZNRF1]] | -0.55 | -0.65 / -0.25 | both halves | 4e-04 |  |
| [[TMEM104]] | -0.54 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.2, 17.5); signed map (30.5, -10.2). **Vector** length 63.2, 9.24% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -0.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP1A1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p13.1 — chr1:116,378,437-116,421,301 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC16179; previously C1orf203, ATP1A1OS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q5TC04](https://www.uniprot.org/uniprotkb/Q5TC04) carries no function annotation.

**Summary**, from NCBI Gene [84852](https://www.ncbi.nlm.nih.gov/gene/84852):

> Predicted to enable U4 snRNA binding activity. Predicted to be involved in formation of quadruple SL/U4/U5/U6 snRNP and spliceosomal tri-snRNP complex assembly. Predicted to be part of U4/U6 x U5 tri-snRNP complex and U6 snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28262) · Entrez [84852](https://www.ncbi.nlm.nih.gov/gene/84852) · UniProt [Q5TC04](https://www.uniprot.org/uniprotkb/Q5TC04) · Ensembl [ENSG00000203865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203865)

## Data

Gene col 12795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12795); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12795]; `tensor/DDL_lfc|DDL_z.npy` [12795]; `embed/gene_vectors.npy` [12795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12795 or target_col == 12795). Every well: [[ATP1A1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP1A1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
