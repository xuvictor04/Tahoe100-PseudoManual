---
symbol: "YBX3"
type: "gene"
col: 683
ensembl_id: "ENSG00000060138"
name: "Y-box binding protein 3"
location: "12p13.2"
module: 14
arm: "+"
pooled_cpm: 294.6
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/014", "written"]
generated_by: "tahoemap"
---

# YBX3

*Y-box binding protein 3* — 12p13.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> YBX3 is a cold-shock-domain protein, the less-studied paralogue of YBX1 (also called DBPA or ZONAB), whose best-supported function is post-transcriptional rather than transcriptional.

## What it is

YBX3 carries a single cold-shock domain and a long charged tail, the same architecture as YBX1, and binds both single-stranded DNA and RNA. Early work treated it as a transcription factor: as ZONAB it was found bound to the tight-junction protein ZO-1 and regulating ErbB-2 expression, and later work from the same group had it sequestered by ZO-1 and released at low cell density to drive proliferation-associated transcription. The stronger recent evidence points the other way — YBX3 binds mRNAs directly and sets the abundance of solute-carrier transcripts, with depletion reducing amino-acid import, though which transporters are affected differs between cell systems. Beyond this the literature is genuinely thin next to YBX1's, with most claims resting on one or two systems.

## What is uncertain

Whether YBX3 is a sequence-specific transcription factor at all is unsettled. Cold-shock domains bind nucleic acid with modest specificity, so an inferred regulon may reflect co-expression with an RNA-binding programme rather than promoter occupancy. If YBX3 acts mainly by stabilising transcripts, "activity" read off target mRNA means something different for it than for a bona fide transcription factor. Its regulon also cannot be cleanly separated from YBX1, which is more abundant and more promiscuous. Extreme ends of a ranking are where artefacts concentrate, and this gene sat at one in the earlier MG53/p53 study.

## References

- Balda & Matter, 2000, EMBO Journal — identified ZONAB (DbpA/YBX3) as a Y-box factor that binds the tight-junction protein ZO-1, and showed the two together regulate ErbB-2 expression.
- Cooke et al., 2019, Cell Reports — showed YBX3 binds mRNAs and controls amino-acid levels by setting SLC transporter transcript abundance.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +9.2, q 1e-17, up in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.11× (z +5.4, q 7e-06, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.280× (z -17.6, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNL1]] (+0.59, fdr 1e-05), [[BCL6]] (+0.57, fdr 1e-05), [[RASGEF1B]] (+0.56, fdr 2e-05); moves opposite to [[FBXW2]] (-0.54, fdr 3e-05), [[TBC1D24]] (-0.49, fdr 5e-05), [[CNEP1R1]] (-0.49, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 8 go from it, the strongest it → [[CCL20]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +9.2 | 1e-17 | 39/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.52×** | +7.8 | 2e-12 | 24/44 (NCI-H1792, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.4 | 3e-11 | 30/40 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +6.0 | 3e-07 | 32/41 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +5.4 | 7e-06 | 29/44 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +5.3 | 9e-06 | 37/45 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.37×** | +4.3 | 0.001 | 28/44 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.3 | 0.002 | 30/43 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 23/45 (SNU-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.012 | 27/46 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.30×** | +3.6 | 0.014 | 24/44 (RPMI-7951, A498, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.070 | 26/45 (HOP62, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.10 | 17/44 (RKO, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.280×** | -17.6 | 0e+00 | 43/44 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -16.2 | 0e+00 | 44/44 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -11.8 | 1e-29 | 40/44 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -4.5 | 0.001 | 28/44 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -4.4 | 0.001 | 33/44 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.835× | -3.3 | 0.099 | 16/44 (H4, NCI-H2347, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.660× | -3.0 | 0.21 | 21/45 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 1,669 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0686× (z -33.1) |
| [[LOX-IMVI (line)]] | wt | 733 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -22.5) |
| [[NCI-H460 (line)]] | wt | 396 | 2 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.91× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.190× (z -17.3) |
| [[A498 (line)]] | wt | 191 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.9) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.245× (z -13.0) |
| [[A549 (line)]] | wt | 323 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.183× (z -19.9) |
| [[H4 (line)]] | wt | 294 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.136× (z -18.1) |
| [[RKO (line)]] | wt | 244 | 1 | 4 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.93× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.195× (z -17.6) |
| [[SK-MEL-2 (line)]] | alt | 199 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -17.1) |
| [[SW48 (line)]] | wt | 265 | 2 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.92× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -16.4) |
| [[SW480 (line)]] | alt | 256 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.177× (z -17.5) |
| [[A-427 (line)]] | wt | 670 | 2 | 2 | [[TAK-901 (drug)]] 5 µM 6.46× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.374× (z -10.5) |
| [[HOP62 (line)]] | alt | 249 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.1) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.217× (z -13.3) |
| [[Hs 766T (line)]] | wt | 427 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -16.3) |
| [[HT-29 (line)]] | alt | 268 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.268× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 270 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.154× (z -15.8) |
| [[KATO III (line)]] | alt | 171 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 117 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.5) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.227× (z -13.0) |
| [[BT-474 (line)]] | alt | 232 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -12.0) |
| [[C32 (line)]] | wt | 210 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 8.05× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.193× (z -13.5) |
| [[COLO 205 (line)]] | alt | 232 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -13.1) |
| [[J82 (line)]] | alt | 207 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.2) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 5 µM 0.283× (z -11.1) |
| [[LoVo (line)]] | wt | 365 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -17.6) |
| [[LS 180 (line)]] | wt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 255 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 334 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 505 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.358× (z -12.3) |
| [[PANC-1 (line)]] | alt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -19.3) |
| [[SW 1271 (line)]] | alt | 713 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -13.5) |
| [[SW 900 (line)]] | alt | 359 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -13.9) |
| [[C-33 A (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 263 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.388× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 381 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 321 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.5) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[RPMI-7951 (line)]] | alt | 145 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.5) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[AN3 CA (line)]] | alt | 156 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.247× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[CHP-212 (line)]] | wt | 168 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -9.6) |
| [[SNU-1 (line)]] | wt | 208 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 194 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -12.1) |
| [[SW1417 (line)]] | alt | 172 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -9.4) |
| [[A-172 (line)]] | wt | 69.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNL1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[BCL6]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RASGEF1B]] | +0.56 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CXCL2]] | +0.53 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[TLE4]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MAFF]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[EPS15-AS1]] | +0.51 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[FBXO32]] | +0.51 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[ANXA2R-AS1]] | +0.51 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[CEBPD]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[HIVEP2]] | +0.50 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[TAFA2]] | +0.50 | +0.39 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D24]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[CNEP1R1]] | -0.49 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[STIMATE]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[GPR180]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[ELMOD2]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[YIF1B]] | -0.45 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[ZNF445]] | -0.45 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[DPM2]] | -0.45 | -0.32 / -0.36 | both halves | 1e-04 |  |
| [[SNRNP40]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZDHHC6]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[AP3M2]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises YBX3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CLDN16]] | B | CLDN16 activity raises YBX3's level | lines that do not express CLDN16 (27) vs lines expressing it (23) | 1.85× lower at baseline in the lines without CLDN16 | 0.067 | ⚠ within organs, on part of the lines; also absent: DAW1, ENSG00000257869, ENSG00000255029 |
| [[DRAM1]] | B | DRAM1 activity raises YBX3's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.95× lower at baseline in the lines without DRAM1 | 0.071 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | C | YBX3 activity raises CCL20's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without YBX3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[HHAT]] | C | YBX3 activity raises HHAT's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without YBX3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[TRAIP]] | C | YBX3 activity lowers TRAIP's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.38× higher at baseline in the lines without YBX3 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent |
| [[ABCA10]] | C | YBX3 activity raises ABCA10's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[CXCL2]] | C | YBX3 activity raises CXCL2's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[REV3L]] | C | YBX3 activity lowers REV3L's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.67× higher at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[STAT4]] | C | YBX3 activity raises STAT4's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |
| [[ZNF445]] | C | YBX3 activity lowers ZNF445's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.25× higher at baseline in the lines without YBX3 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 15.4); signed map (41.0, 5.1). **Vector** length 128, 45.5% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +7.4 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -16.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Y-box binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,699,089-10,723,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dbpA, ZONAB, CSDA1; previously CSDA |
| Gene groups (HGNC) | Y-box binding proteins; Cold shock domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P16989](https://www.uniprot.org/uniprotkb/P16989) (Y-box-binding protein 3):

> Binds to the GM-CSF promoter. Seems to act as a repressor. Also binds to full-length mRNA and to short RNA sequences containing the consensus site 5'-UCCAUCA-3'. May have a role in translation repression (By similarity).

**Summary**, from NCBI Gene [8531](https://www.ncbi.nlm.nih.gov/gene/8531):

> Enables RNA binding activity. Involved in cellular hyperosmotic response; cellular response to tumor necrosis factor; and negative regulation of programmed cell death. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2428) · Entrez [8531](https://www.ncbi.nlm.nih.gov/gene/8531) · UniProt [P16989](https://www.uniprot.org/uniprotkb/P16989) · Ensembl [ENSG00000060138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060138)

## Data

Gene col 683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 683); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 683]; `tensor/DDL_lfc|DDL_z.npy` [683]; `embed/gene_vectors.npy` [683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 683 or target_col == 683). Every well: [[YBX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/YBX3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
