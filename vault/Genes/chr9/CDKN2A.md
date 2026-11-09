---
symbol: "CDKN2A"
type: "gene"
col: 7231
ensembl_id: "ENSG00000147889"
name: "cyclin dependent kinase inhibitor 2A"
location: "9p21.3"
module: 14
arm: "+"
pooled_cpm: 62.67
n_lines_expressing: 28
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/014", "written"]
generated_by: "tahoemap"
---

# CDKN2A

*cyclin dependent kinase inhibitor 2A* — 9p21.3

> [!summary] In one line
> CDKN2A is not one gene but one locus encoding two unrelated tumour suppressors from overlapping exons — p16^INK4a^, which holds the RB pathway on, and p14ARF, which stabilises p53 by inhibiting MDM2.

## What it is

The locus uses alternative first exons and two reading frames across shared exons 2 and 3. Transcripts beginning at exon 1α give p16^INK4a^, an INK4-family inhibitor of CDK4 and CDK6; blocking those kinases keeps RB hypophosphorylated and E2F targets off, so p16 acts entirely within the RB arm of cell-cycle control. Transcripts beginning at exon 1β are read in a different frame (hence ARF, alternative reading frame) to give p14ARF — in mouse, p19Arf — a nucleolar protein with no relationship to p16 in sequence or structure. ARF binds MDM2, sequesters and inhibits it, and so blocks MDM2-mediated ubiquitination of p53, stabilising it. Critically, ARF is induced by oncogenic signalling — E2F, MYC, RAS — which makes it the route by which hyperproliferative signals, rather than DNA damage, activate p53. One locus therefore feeds both of the two pathways most often broken in human cancer.

CDKN2A is among the most frequently inactivated regions in the cancer genome: homozygous deletion, promoter methylation and point mutation all occur, and germline mutation underlies familial melanoma. The deletions are often large, and commonly remove the neighbouring MTAP gene — the basis for the MAT2A and PRMT5 synthetic-lethality strategies now pursued in MTAP-deleted tumours. In cultured cancer cell lines the locus is lost at high frequency, which matters more here than its mutation spectrum.

## What is uncertain

The most important caveat is measurement, not biology: a gene-level expression count for CDKN2A collapses p16 and p14ARF, two proteins acting on different pathways, because they share most of their exons. A CDKN2A number is ambiguous by construction unless the exon-1α and exon-1β transcripts are resolved, which short-read 3′ single-cell data generally cannot do. In lines where the locus is deleted, low counts report copy loss rather than regulation, and the deletion also removes MTAP, so neighbouring-gene signals are not independent. On the biology, how much of ARF's tumour-suppressive activity runs through p53 is genuinely contested — p53-independent ARF functions have been described in both mouse and human systems — and the mouse-to-human mapping is imperfect enough that murine p19Arf results do not transfer cleanly.

## References

- Serrano, Hannon & Beach, 1993, Nature — identified p16 as a specific inhibitor of cyclin D/CDK4.
- Kamb et al., 1994, Science — mapped the locus as a cell-cycle regulator deleted across many tumour types.
- Quelle et al., 1995, Cell — showed the alternative reading frames of INK4a encode two unrelated growth-arresting proteins.
- Pomerantz et al., 1998, Cell — ARF interacts with MDM2 and neutralises its inhibition of p53.
- Zhang, Xiong & Yarbrough, 1998, Cell — ARF promotes MDM2 degradation and stabilises p53, so locus deletion impairs both the RB and p53 pathways.
- Sherr, 2006, Nature Reviews Cancer — argued the case for p53-independent ARF functions is unsettled.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.40× (z +6.1, q 5e-07, up in 19 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.295× (z -23.0, q 0e+00, down in 25 of 26 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.301× (z -22.6, q 0e+00, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2B-AS1]] (+0.57, fdr 1e-05, ⚠ same locus), [[REL]] (+0.56, fdr 2e-05), [[CDKN2B]] (+0.56, fdr 3e-05, ⚠ same locus), [[ELF3-AS1]] (+0.55, fdr 3e-05), [[MVP-DT]] (+0.55, fdr 3e-05); moves opposite to [[ZFYVE9]] (-0.56, fdr 1e-05), [[NSUN2]] (-0.53, fdr 3e-05), [[C16orf74]] (-0.53, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDKN2B]] → it (grade B ⚠); 5 go from it, the strongest it → [[CDKN2B-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +6.1 | 5e-07 | 19/26 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +4.9 | 2e-04 | 14/26 (HT-29, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 3e-04 | 16/26 (HT-29, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.23×** | +4.4 | 0.002 | 15/28 (HT-29, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.8 | 0.018 | 12/25 (NCI-H2030, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.7 | 0.018 | 11/26 (J82, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.15× | +3.7 | 0.019 | 8/27 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.072 | 8/26 (HT-29, AsPC-1, …) | all doses, stronger at high dose |  |
| [[BI-3406 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.073 | 10/25 (AsPC-1, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.079 | 14/26 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose | low cells (technical?) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.12× | +3.1 | 0.095 | 0/26 | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.095 | 13/25 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.095 | 5/26 (AsPC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.295×** | -23.0 | 0e+00 | 25/26 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.301×** | -22.6 | 0e+00 | 26/26 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.351×** | -19.7 | 0e+00 | 24/26 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.564×** | -10.8 | 7e-25 | 20/26 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.489×** | -7.0 | 2e-10 | 19/26 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.694×** | -6.5 | 8e-09 | 20/26 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -5.8 | 6e-07 | 2/27 (NCI-H1573, CHP-212) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -5.6 | 2e-06 | 14/26 (HT-29, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.748×** | -5.2 | 1e-05 | 15/26 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.824×** | -5.1 | 2e-05 | 16/25 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.766×** | -5.0 | 3e-05 | 15/25 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -4.8 | 6e-05 | 13/26 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.776×** | -4.8 | 8e-05 | 15/26 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.780×** | -4.7 | 1e-04 | 14/26 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.639×** | -4.4 | 4e-04 | 14/24 (NCI-H1792, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -4.3 | 5e-04 | 13/26 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.6 | 0.009 | 11/26 (Hs 766T, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.018 | 7/26 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.889× | -3.1 | 0.047 | 6/26 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.051 | 9/28 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.854× | -3.0 | 0.071 | 9/26 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.896× | -2.9 | 0.082 | 4/26 (SW480, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 193 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0549× (z -30.7) |
| [[Hs 766T (line)]] | wt | 404 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0874× (z -27.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0917× (z -26.7) |
| [[HT-29 (line)]] | alt | 135 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -19.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.249× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 154 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -11.1) |
| [[COLO 205 (line)]] | alt | 113 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0842× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 1 | 4 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.23× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.229× (z -11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.236× (z -11.4) |
| [[SW480 (line)]] | alt | 129 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -29.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -25.4) |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -17.6) |
| [[HOP62 (line)]] | alt | 90.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -15.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.175× (z -13.8) |
| [[LoVo (line)]] | wt | 31.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.152× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.236× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 81.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -16.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 63.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -11.2) |
| [[SHP-77 (line)]] | alt | 85.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -15.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -13.3) |
| [[SNU-423 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -18.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -15.0) |
| [[C-33 A (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -11.7) |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.6) |
| [[A-172 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2B-AS1]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[REL]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 | STRING 430 |
| [[CDKN2B]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 | same gene group; pathway: HALLMARK_P53_PATHWAY; STRING 951; ⚠ same locus (7.6 kb, same strand: neighbours can correlate without regulation) |
| [[ELF3-AS1]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MVP-DT]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PIK3IP1]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GBP2]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[VNN1]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[KMO]] | +0.53 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[CHD2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[DUOX2]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RND1]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[DDR1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ARHGAP42]] | +0.52 | +0.41 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE9]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[C16orf74]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[THSD4]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ZHX3]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[UAP1]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ABCC5]] | -0.47 | -0.42 / -0.57 | both halves | 4e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[THBD]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[NR2E3]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[POLR3B]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TOMM70]] | -0.47 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[LAMB1]] | -0.46 | -0.37 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2B]] | B | CDKN2B activity raises CDKN2A's level | recorded loss-of-function mutation of CDKN2B in 13 lines vs 37 not recorded | 7.11× lower at baseline in the CDKN2B-altered lines | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[TNFAIP2]] | B | TNFAIP2 activity strengthens CDKN2A's drug response | lines that do not express TNFAIP2 (12) vs lines expressing it (15) | the lines without TNFAIP2 respond 0.71× as strongly (z diff +1.03); strongest at Doxorubicin (hydrochloride) 5 µM: 0.81x vs 0.67x (z diff +1.7) | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1; target measured in part of the lines; artifact flags |
| [[CGNL1]] | B | CGNL1 activity raises CDKN2A's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without CGNL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[CTSS]] | B | CTSS activity raises CDKN2A's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without CTSS | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[CDKN2B]] | C | CDKN2B activity raises CDKN2A's level | lines that do not express CDKN2B (12) vs lines expressing it (38) | 8.45× lower at baseline in the lines without CDKN2B | 7e-04 | ⚠ within organs, on part of the lines; deletion recorded too; co-occurs with CDKN2A; also absent: ENSG00000264545, CDKN2A, MTAP; co-absent with the target |
| [[CDKN2B-AS1]] | C | CDKN2B-AS1 activity raises CDKN2A's level | lines that do not express CDKN2B-AS1 (18) vs lines expressing it (32) | 7.41× lower at baseline in the lines without CDKN2B-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDKN2A, SLCO6A1, CDKN2B; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2B-AS1]] | B | CDKN2A activity strengthens CDKN2B-AS1's drug response | lines that do not express CDKN2A (5) vs lines expressing it (25) | the lines without CDKN2A respond 0.44× as strongly (z diff +2.68); strongest at Panobinostat 5 µM: 0.54x vs 0.20x (z diff +5.6) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; target measured in part of the lines; artifact flags |
| [[CGNL1]] | B | CDKN2A activity raises CGNL1's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without CDKN2A | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE |
| [[DUOX2]] | B | CDKN2A activity raises DUOX2's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without CDKN2A | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE |
| [[CDKN2B]] | C | CDKN2A activity raises CDKN2B's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 4.04× lower at baseline in the lines without CDKN2A | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; co-absent with the target |
| [[CDKN2B-AS1]] | C | CDKN2A activity raises CDKN2B-AS1's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 4.85× lower at baseline in the lines without CDKN2A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 2.5); signed map (48.1, 8.2). **Vector** length 81.1, 20.4% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -5.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:21,967,752-21,995,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDK4I, p16, INK4a, MTS1, CMM2, ARF, p19, p14; previously CDKN2, MLM |
| Gene groups (HGNC) | Cyclin dependent kinase inhibitor 2 family |
| Hallmark sets | ALLOGRAFT_REJECTION, P53_PATHWAY, E2F_TARGETS |
| Reactome | 46 pathways, smallest: Diseases of Cellular Senescence; Diseases of cellular response to stress; Evasion of Oncogene Induced Senescence Due to Defective p16INK4A binding to CDK4 and CDK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [P42771](https://www.uniprot.org/uniprotkb/P42771) (Cyclin-dependent kinase inhibitor 2A):

> Acts as a negative regulator of the proliferation of normal cells by interacting strongly with CDK4 and CDK6. This inhibits their ability to interact with cyclins D and to phosphorylate the retinoblastoma protein.

**Summary**, from NCBI Gene [1029](https://www.ncbi.nlm.nih.gov/gene/1029):

> This gene generates several transcript variants which differ in their first exons. At least three alternatively spliced variants encoding distinct proteins have been reported, two of which encode structurally related isoforms known to function as inhibitors of CDK4 kinase. The remaining transcript includes an alternate first exon located 20 Kb upstream of the remainder of the gene; this transcript contains an alternate open reading frame (ARF) that specifies a protein which is structurally …

**Accessions** — [HGNC:1787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1787) · Entrez [1029](https://www.ncbi.nlm.nih.gov/gene/1029) · UniProt [P42771](https://www.uniprot.org/uniprotkb/P42771) · Ensembl [ENSG00000147889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147889)

## Data

Gene col 7231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7231); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7231]; `tensor/DDL_lfc|DDL_z.npy` [7231]; `embed/gene_vectors.npy` [7231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7231 or target_col == 7231). Every well: [[CDKN2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CDKN2A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
