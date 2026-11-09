---
symbol: "PPIB"
type: "gene"
col: 9357
ensembl_id: "ENSG00000166794"
name: "peptidylprolyl isomerase B"
location: "15q22.31"
module: 42
arm: "+"
pooled_cpm: 109.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PPIB

*peptidylprolyl isomerase B* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +8.5, q 7e-15, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.74× (z +3.5, q 0.062, up in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-427 6.89×, LOX-IMVI 5.15×, C32 4.95×, SNU-423 4.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 6.15×, LOX-IMVI 5.32×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.450× (z -9.8, q 8e-20, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (NCI-H2030 0.243×, RPMI-7951 0.252×, A-427 0.228×, HS-578T 0.287×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED9]] (+0.79, fdr 7e-06), [[P4HB]] (+0.71, fdr 7e-06), [[PDIA4]] (+0.70, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A-427 6.89×, LOX-IMVI 5.15×, C32 4.95×, SNU-423 4.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 6.15×, LOX-IMVI 5.32×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +8.5 | 7e-15 | 46/49 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.1 | 4e-10 | 39/44 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +4.4 | 0.002 | 38/45 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.7 | 0.030 | 4/50 (SHP-77, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.062 | 37/47 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.69× | +3.3 | 0.10 | 39/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.67× | +3.2 | 0.10 | 34/48 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | 1.44× | +3.2 | 0.10 | 28/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 1.65× | +3.1 | 0.11 | 31/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (NCI-H2030 0.243×, RPMI-7951 0.252×, A-427 0.228×, HS-578T 0.287×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.450×** | -9.8 | 8e-20 | 46/48 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.677× | -3.4 | 0.21 | 34/48 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 0.775× | -3.1 | 0.37 | 29/48 (LS 180, A-427, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.691× | -3.0 | 0.37 | 26/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 49.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 56.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 164 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.1) |
| [[A498 (line)]] | wt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.4) |
| [[C-33 A (line)]] | alt | 62.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.8) |
| [[HCT15 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) |
| [[HS-578T (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.7) |
| [[HT-29 (line)]] | alt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.6) |
| [[J82 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.2) |
| [[KATO III (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 71.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 231 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.4) |
| [[SHP-77 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.0) |
| [[SNU-423 (line)]] | alt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 92.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -8.6) |
| [[SW480 (line)]] | alt | 66.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[A-172 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 148 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED9]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[P4HB]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | pathway: Collagen biosynthesis and modifying enzymes; STRING 966 |
| [[PDIA4]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 | STRING 994 |
| [[MANF]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CALU]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 424 |
| [[CALR]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 | STRING 987 |
| [[HSP90B1]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | STRING 994 |
| [[DAD1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CHCHD2]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GORASP2]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 | STRING 849 |
| [[TMED7-TICAM2]] | +0.63 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -31.3); signed map (-54.1, 8.7). **Vector** length 108, 44.4% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.59 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.54 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +1.8 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -9.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Flutamide (drug)]] 0.5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,155,740-64,163,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYPB, OI9, PPIase, B, CYP-S1, SCYLP |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23284](https://www.uniprot.org/uniprotkb/P23284) (Peptidyl-prolyl cis-trans isomerase B):

> Peptidyl-prolyl cis-trans isomerase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding.

**Summary**, from NCBI Gene [5479](https://www.ncbi.nlm.nih.gov/gene/5479):

> The protein encoded by this gene is a cyclosporine-binding protein and is mainly located within the endoplasmic reticulum. It is associated with the secretory pathway and released in biological fluids. This protein can bind to cells derived from T- and B-lymphocytes, and may regulate cyclosporine A-mediated immunosuppression. Variants have been identified in this protein that give rise to recessive forms of osteogenesis imperfecta. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:9255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9255) · Entrez [5479](https://www.ncbi.nlm.nih.gov/gene/5479) · UniProt [P23284](https://www.uniprot.org/uniprotkb/P23284) · Ensembl [ENSG00000166794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166794)

## Data

Gene col 9357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9357); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9357]; `tensor/DDL_lfc|DDL_z.npy` [9357]; `embed/gene_vectors.npy` [9357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9357 or target_col == 9357). Every well: [[PPIB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
